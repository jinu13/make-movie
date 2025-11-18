#!/usr/bin/env python3
"""
실사 비디오 생성 API 엔드포인트

Gemini 2.5 Pro + Qwen LoRA + Wan2.2 i2v 파이프라인
"""

import sys
import os
from typing import Optional
from pathlib import Path

from fastapi import BackgroundTasks, Depends, Request
from loguru import logger

# realistic_automation 모듈 경로 추가
sys.path.append(str(Path(__file__).parent.parent.parent.parent.parent))

from app.config import config
from app.controllers import base
from app.controllers.manager.memory_manager import InMemoryTaskManager
from app.controllers.manager.redis_manager import RedisTaskManager
from app.controllers.v1.base import new_router
from app.models.exception import HttpException
from app.models.schema import TaskResponse
from app.services import state as sm
from app.utils import utils

from pydantic import BaseModel, Field

# realistic_automation 모듈 임포트
try:
    from realistic_automation.realistic_orchestrator import RealisticOrchestrator
    REALISTIC_ENABLED = True
except ImportError as e:
    logger.warning(f"⚠️ realistic_automation 모듈 로드 실패: {e}")
    REALISTIC_ENABLED = False


# 라우터 생성
router = new_router()

# 태스크 매니저 설정
_enable_redis = config.app.get("enable_redis", False)
_redis_host = config.app.get("redis_host", "localhost")
_redis_port = config.app.get("redis_port", 6379)
_redis_db = config.app.get("redis_db", 0)
_redis_password = config.app.get("redis_password", None)
_max_concurrent_tasks = config.app.get("max_concurrent_tasks", 5)

redis_url = f"redis://:{_redis_password}@{_redis_host}:{_redis_port}/{_redis_db}"

if _enable_redis:
    task_manager = RedisTaskManager(
        max_concurrent_tasks=_max_concurrent_tasks, redis_url=redis_url
    )
else:
    task_manager = InMemoryTaskManager(max_concurrent_tasks=_max_concurrent_tasks)


# Request 스키마
class RealisticVideoRequest(BaseModel):
    """실사 비디오 생성 요청"""

    topic: str = Field(..., description="비디오 주제 (예: '커피 한 잔의 여유')")
    num_scenes: int = Field(3, ge=1, le=10, description="생성할 장면 수 (1-10)")
    language: str = Field("ko", description="내레이션 언어 (ko, en, ja, zh)")
    resolution: str = Field("720x1280", description="비디오 해상도 (WxH)")
    add_bgm: bool = Field(True, description="배경음악 추가 여부")
    bgm_path: Optional[str] = Field(None, description="사용자 BGM 경로 (없으면 자동 선택)")


# 백그라운드 태스크 실행 함수
def run_realistic_video_generation(task_id: str, params: RealisticVideoRequest):
    """
    실사 비디오 생성 백그라운드 작업
    """
    try:
        logger.info(f"🎬 Realistic 비디오 생성 시작: {task_id}")
        logger.info(f"  주제: {params.topic}")
        logger.info(f"  장면 수: {params.num_scenes}")

        # 상태 업데이트: 진행 중
        sm.state.update_task(task_id, state="processing", progress=0)

        # Orchestrator 초기화
        orchestrator = RealisticOrchestrator(
            comfyui_url=config.app.get("comfyui_url", "http://localhost:8188"),
            gemini_api_key=os.getenv("GEMINI_API_KEY"),
        )

        # 비디오 생성
        sm.state.update_task(task_id, state="processing", progress=10)

        result = orchestrator.generate_video(
            topic=params.topic,
            num_scenes=params.num_scenes,
            language=params.language,
            resolution=params.resolution,
            add_bgm=params.add_bgm,
            bgm_path=params.bgm_path,
        )

        # 결과 파일 경로 구성
        video_path = result.final_video_path

        # 상태 업데이트: 완료
        sm.state.update_task(
            task_id,
            state="completed",
            progress=100,
            videos=[video_path],
            metadata={
                "topic": params.topic,
                "num_scenes": params.num_scenes,
                "script": result.script,
                "scene_videos": result.scene_videos,
                "total_duration": result.total_duration,
            }
        )

        logger.success(f"✅ Realistic 비디오 생성 완료: {task_id}")
        logger.info(f"  출력: {video_path}")

    except Exception as e:
        logger.error(f"❌ Realistic 비디오 생성 실패: {task_id}")
        logger.exception(e)

        # 상태 업데이트: 실패
        sm.state.update_task(
            task_id,
            state="failed",
            progress=0,
            error=str(e)
        )


@router.post("/realistic/videos", response_model=TaskResponse, summary="Generate realistic video")
def create_realistic_video(
    background_tasks: BackgroundTasks,
    request: Request,
    body: RealisticVideoRequest
):
    """
    실사 스타일 비디오 생성

    워크플로우:
    1. Gemini 2.5 Pro로 대본 + 프롬프트 생성
    2. Qwen LoRA로 첫 장면 이미지 생성
    3. Wan2.2 i2v로 비디오 변환 (끝→시작 연결)
    4. MMAudio로 효과음 추가 (옵션)
    5. TTS + 자막 + BGM 합성

    Args:
        background_tasks: FastAPI 백그라운드 작업
        request: FastAPI 요청 객체
        body: 실사 비디오 생성 요청 파라미터

    Returns:
        TaskResponse: 작업 ID 및 상태

    Raises:
        HttpException: realistic_automation 비활성화 또는 생성 실패
    """

    # realistic_automation 활성화 확인
    if not REALISTIC_ENABLED:
        raise HttpException(
            status_code=503,
            message="realistic_automation 모듈이 비활성화되었습니다. 설치 후 다시 시도하세요."
        )

    # 작업 ID 생성
    task_id = utils.get_uuid()
    request_id = base.get_task_id(request)

    try:
        # 작업 정보 구성
        task = {
            "task_id": task_id,
            "request_id": request_id,
            "type": "realistic_video",
            "params": body.model_dump(),
        }

        # 상태 초기화
        sm.state.update_task(task_id, state="pending", progress=0)

        # 백그라운드 작업 추가
        task_manager.add_task(
            run_realistic_video_generation,
            task_id=task_id,
            params=body
        )

        logger.success(f"📝 Realistic 비디오 작업 생성: {utils.to_json(task)}")

        return utils.get_response(200, task)

    except ValueError as e:
        raise HttpException(
            task_id=task_id,
            status_code=400,
            message=f"{request_id}: {str(e)}"
        )
    except Exception as e:
        logger.exception(f"❌ 작업 생성 실패: {task_id}")
        raise HttpException(
            task_id=task_id,
            status_code=500,
            message=f"{request_id}: 내부 서버 오류 - {str(e)}"
        )


@router.get("/realistic/health", summary="Check realistic module health")
def check_realistic_health():
    """
    realistic_automation 모듈 상태 확인

    Returns:
        dict: 모듈 활성화 상태 및 버전 정보
    """
    if REALISTIC_ENABLED:
        try:
            from realistic_automation import __version__
            return {
                "status": "ok",
                "enabled": True,
                "version": __version__,
                "message": "realistic_automation 모듈이 정상 작동합니다."
            }
        except Exception as e:
            return {
                "status": "error",
                "enabled": True,
                "version": "unknown",
                "message": f"모듈 로드는 성공했으나 버전 확인 실패: {str(e)}"
            }
    else:
        return {
            "status": "disabled",
            "enabled": False,
            "version": None,
            "message": "realistic_automation 모듈이 설치되지 않았습니다."
        }
