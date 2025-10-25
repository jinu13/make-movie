<div align="center">
<h1 align="center">MoneyPrinterTurbo 💸</h1>

<p align="center">
  <a href="https://github.com/harry0703/MoneyPrinterTurbo/stargazers"><img src="https://img.shields.io/github/stars/harry0703/MoneyPrinterTurbo.svg?style=for-the-badge" alt="Stargazers"></a>
  <a href="https://github.com/harry0703/MoneyPrinterTurbo/issues"><img src="https://img.shields.io/github/issues/harry0703/MoneyPrinterTurbo.svg?style=for-the-badge" alt="Issues"></a>
  <a href="https://github.com/harry0703/MoneyPrinterTurbo/network/members"><img src="https://img.shields.io/github/forks/harry0703/MoneyPrinterTurbo.svg?style=for-the-badge" alt="Forks"></a>
  <a href="https://github.com/harry0703/MoneyPrinterTurbo/blob/main/LICENSE"><img src="https://img.shields.io/github/license/harry0703/MoneyPrinterTurbo.svg?style=for-the-badge" alt="License"></a>
</p>
<br>
<h3><a href="README.md">简体中文</a> | <a href="README-en.md">English</a> | 한국어</h3>
<div align="center">
  <a href="https://trendshift.io/repositories/8731" target="_blank"><img src="https://trendshift.io/api/badge/repositories/8731" alt="harry0703%2FMoneyPrinterTurbo | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</div>
<br>
비디오 <b>주제</b> 또는 <b>키워드</b>만 제공하면, 자동으로 비디오 대본, 비디오 소스, 비디오 자막, 배경 음악을 생성하고 고화질 숏폼 비디오를 합성합니다.
<br>

<h4>Web 인터페이스</h4>

![](docs/webui.jpg)

<h4>API 인터페이스</h4>

![](docs/api.jpg)

</div>

## 특별 감사 🙏

이 프로젝트의 **배포**와 **사용**이 일부 초보 사용자에게는 **다소 어려울 수 있어**, 특별히 **RecCloud(AI 지능형 멀티미디어 서비스 플랫폼)**에 감사드립니다. 이 프로젝트를 기반으로 무료 `AI 비디오 생성기` 서비스를 제공하여 배포 없이 온라인으로 직접 사용할 수 있어 매우 편리합니다.

- 중국어 버전: https://reccloud.cn
- 영어 버전: https://reccloud.com

![](docs/reccloud.cn.jpg)

## 스폰서 감사 🙏

이 프로젝트의 지속적인 업데이트와 유지보수를 가능하게 해준 PicWish https://picwish.cn 의 지원과 후원에 감사드립니다.

PicWish는 **이미지 처리 분야**에 집중하여 복잡한 작업을 극도로 간소화하고 다양한 **이미지 처리 도구**를 제공하여 진정으로 이미지 처리를 더 쉽게 만듭니다.

![picwish.jpg](docs/picwish.jpg)

## 주요 기능 🎯

- [x] 완전한 **MVC 아키텍처**, **명확한 코드 구조**, 유지보수 용이, `API` 및 `Web 인터페이스` 지원
- [x] 비디오 대본 **AI 자동 생성** 지원, **사용자 정의 대본**도 가능
- [x] 다양한 **고화질 비디오** 해상도 지원
    - [x] 세로형 9:16, `1080x1920`
    - [x] 가로형 16:9, `1920x1080`
- [x] **일괄 비디오 생성** 지원, 여러 개를 한 번에 생성하고 가장 만족스러운 것을 선택
- [x] **비디오 클립 길이** 설정 지원, 소스 전환 빈도 조절 가능
- [x] **한국어**, **중국어** 및 **영어** 비디오 대본 지원
- [x] **다양한 음성** 합성 지원, **실시간 미리듣기** 가능
- [x] **자막 생성** 지원, `폰트`, `위치`, `색상`, `크기` 조정 가능, `자막 테두리` 설정 지원
- [x] **배경 음악** 지원, 랜덤 또는 지정된 음악 파일 사용, `배경 음악 볼륨` 설정 가능
- [x] 비디오 소스 **고화질**이며 **저작권 없음**, **로컬 소스** 사용도 가능
- [x] **OpenAI**, **Moonshot**, **Azure**, **gpt4free**, **one-api**, **通义千问**, **Google Gemini**, **Ollama**, **DeepSeek**, **文心一言**, **Pollinations** 등 다양한 모델 통합 지원
    - 한국 사용자는 **DeepSeek** 또는 **Moonshot**을 대형 모델 제공자로 사용하는 것을 권장합니다 (국내에서 직접 접근 가능, VPN 불필요. 가입 시 크레딧 제공, 기본적으로 충분함)


### 향후 계획 📅

- [ ] GPT-SoVITS 더빙 지원
- [ ] 음성 합성 최적화, 대형 모델 활용으로 더 자연스럽고 감정이 풍부한 음성 생성
- [ ] 비디오 전환 효과 추가로 더 부드러운 영상 제작
- [ ] 더 많은 비디오 소스 추가, 비디오 소스와 대본 간의 매칭도 최적화
- [ ] 비디오 길이 옵션 추가: 짧음, 중간, 길음
- [ ] OpenAI TTS 등 더 많은 음성 합성 서비스 제공자 지원
- [ ] YouTube 플랫폼 자동 업로드

## 비디오 데모 📺

### 세로형 9:16

<table>
<thead>
<tr>
<th align="center"><g-emoji class="g-emoji" alias="arrow_forward">▶️</g-emoji> 《생활의 즐거움을 늘리는 방법》</th>
<th align="center"><g-emoji class="g-emoji" alias="arrow_forward">▶️</g-emoji> 《돈의 역할》<br>더 실제적인 합성 음성</th>
<th align="center"><g-emoji class="g-emoji" alias="arrow_forward">▶️</g-emoji> 《인생의 의미는 무엇인가》</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center"><video src="https://github.com/harry0703/MoneyPrinterTurbo/assets/4928832/a84d33d5-27a2-4aba-8fd0-9fb2bd91c6a6"></video></td>
<td align="center"><video src="https://github.com/harry0703/MoneyPrinterTurbo/assets/4928832/af2f3b0b-002e-49fe-b161-18ba91c055e8"></video></td>
<td align="center"><video src="https://github.com/harry0703/MoneyPrinterTurbo/assets/4928832/112c9564-d52b-4472-99ad-970b75f66476"></video></td>
</tr>
</tbody>
</table>

### 가로형 16:9

<table>
<thead>
<tr>
<th align="center"><g-emoji class="g-emoji" alias="arrow_forward">▶️</g-emoji>《인생의 의미는 무엇인가》</th>
<th align="center"><g-emoji class="g-emoji" alias="arrow_forward">▶️</g-emoji>《왜 운동을 해야 하는가》</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center"><video src="https://github.com/harry0703/MoneyPrinterTurbo/assets/4928832/346ebb15-c55f-47a9-a653-114f08bb8073"></video></td>
<td align="center"><video src="https://github.com/harry0703/MoneyPrinterTurbo/assets/4928832/271f2fae-8283-44a0-8aa0-0ed8f9a6fa87"></video></td>
</tr>
</tbody>
</table>

## 시스템 요구사항 📦

- 최소 CPU **4코어** 이상, 메모리 **4GB** 이상 권장, GPU는 필수 아님
- Windows 10 또는 MacOS 11.0 이상


## 빠른 시작 🚀

### Google Colab에서 실행
로컬 환경 설정 없이, 클릭만으로 Google Colab에서 MoneyPrinterTurbo를 빠르게 체험하세요

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/harry0703/MoneyPrinterTurbo/blob/main/docs/MoneyPrinterTurbo.ipynb)


### Windows 원클릭 시작 패키지

원클릭 시작 패키지를 다운로드하여 압축 해제 후 바로 사용 (경로에 **한글**, **특수문자**, **공백** 없어야 함)

- 百度网盘（v1.2.6）: https://pan.baidu.com/s/1wg0UaIyXpO3SqIpaq790SQ?pwd=sbqx 추출 코드: sbqx
- Google Drive (v1.2.6): https://drive.google.com/file/d/1HsbzfT7XunkrCrHw5ncUjFX8XX4zAuUh/view?usp=sharing

다운로드 후, 먼저 **더블클릭하여** `update.bat`을 실행하여 **최신 코드**로 업데이트하고, `start.bat`을 더블클릭하여 시작

시작 후 자동으로 브라우저가 열립니다 (빈 페이지가 열리면 **Chrome** 또는 **Edge**로 여는 것을 권장)

## 설치 및 배포 📥

### 전제 조건

- 가능한 **한글 경로**를 사용하지 마세요, 예상치 못한 문제가 발생할 수 있습니다
- **네트워크**가 정상적인지 확인하세요, VPN은 `전역 트래픽` 모드를 켜야 합니다

#### ① 코드 복제

```shell
git clone https://github.com/harry0703/MoneyPrinterTurbo.git
```

#### ② 설정 파일 수정 (선택사항, 시작 후 WebUI에서도 설정 가능)

- `config.example.toml` 파일을 복사하여 `config.toml`로 이름 변경
- `config.toml` 파일의 설명에 따라 `pexels_api_keys`와 `llm_provider`를 설정하고, llm_provider에 해당하는 서비스 제공자에 따라 관련 API Key 설정

### Docker 배포 🐳

#### ① Docker 시작

Docker가 설치되지 않았다면 먼저 설치하세요 https://www.docker.com/products/docker-desktop/

Windows 시스템인 경우 Microsoft 문서를 참조하세요:

1. https://learn.microsoft.com/ko-kr/windows/wsl/install
2. https://learn.microsoft.com/ko-kr/windows/wsl/tutorials/wsl-containers

```shell
cd MoneyPrinterTurbo
docker-compose up
```

> 참고: 최신 버전의 docker는 설치 시 플러그인 형태로 docker compose를 자동 설치하므로, 시작 명령이 docker compose up으로 조정됩니다

#### ② Web 인터페이스 접속

브라우저를 열고 http://0.0.0.0:8501 에 접속

#### ③ API 문서 접속

브라우저를 열고 http://0.0.0.0:8080/docs 또는 http://0.0.0.0:8080/redoc 에 접속

### 수동 배포 📦

> 비디오 튜토리얼

- 전체 사용 데모: https://v.douyin.com/iFhnwsKY/
- Windows에서 배포하는 방법: https://v.douyin.com/iFyjoW3M

#### ① 가상 환경 생성

[conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)를 사용하여 python 가상 환경을 생성하는 것을 권장합니다

```shell
git clone https://github.com/harry0703/MoneyPrinterTurbo.git
cd MoneyPrinterTurbo
conda create -n MoneyPrinterTurbo python=3.11
conda activate MoneyPrinterTurbo
pip install -r requirements.txt
```

#### ② ImageMagick 설치

- Windows:
    - https://imagemagick.org/script/download.php 에서 Windows 버전을 다운로드하고, 반드시 **정적 라이브러리** 버전을 선택하세요, 예: ImageMagick-7.1.1-32-Q16-x64-**static**.exe
    - 다운로드한 ImageMagick을 설치하되, **설치 경로를 변경하지 마세요**
    - `설정 파일 config.toml`의 `imagemagick_path`를 **실제 설치 경로**로 수정

- MacOS:
  ```shell
  brew install imagemagick
  ````
- Ubuntu
  ```shell
  sudo apt-get install imagemagick
  ```
- CentOS
  ```shell
  sudo yum install ImageMagick
  ```

#### ③ Web 인터페이스 시작 🌐

MoneyPrinterTurbo 프로젝트 `루트 디렉토리`에서 다음 명령을 실행하세요

###### Windows

```bat
webui.bat
```

###### MacOS 또는 Linux

```shell
sh webui.sh
```

시작 후 자동으로 브라우저가 열립니다 (빈 페이지가 열리면 **Chrome** 또는 **Edge**로 여는 것을 권장)

#### ④ API 서비스 시작 🚀

```shell
python main.py
```

시작 후, `API 문서` http://127.0.0.1:8080/docs 또는 http://127.0.0.1:8080/redoc 에서 직접 온라인으로 인터페이스를 디버그하고 빠르게 체험할 수 있습니다.

## 음성 합성 🗣

지원되는 모든 음성 목록은 다음에서 확인할 수 있습니다: [음성 목록](./docs/voice-list.txt)

2024-04-16 v1.1.2에서 9가지 Azure 음성 합성 음성이 새로 추가되었으며, API KEY 설정이 필요합니다. 이 음성은 더 실제적으로 합성됩니다.

## 자막 생성 📜

현재 2가지 자막 생성 방식을 지원합니다:

- **edge**: 생성 `속도 빠름`, 성능 우수, 컴퓨터 사양 요구 없음, 하지만 품질이 불안정할 수 있음
- **whisper**: 생성 `속도 느림`, 성능 낮음, 컴퓨터 사양에 일정 요구 있음, 하지만 `품질 더 안정적`.

`config.toml` 설정 파일의 `subtitle_provider`를 수정하여 전환할 수 있습니다

`edge` 모드 사용을 권장하며, 생성된 자막 품질이 좋지 않으면 `whisper` 모드로 전환하세요

> 참고:

1. whisper 모드에서는 HuggingFace에서 약 3GB 정도의 모델 파일을 다운로드해야 하므로 네트워크가 원활한지 확인하세요
2. 비워두면 자막이 생성되지 않습니다.

> 국내에서 HuggingFace에 접근할 수 없는 경우, 다음 방법으로 `whisper-large-v3` 모델 파일을 다운로드할 수 있습니다

다운로드 주소:

- 百度网盘: https://pan.baidu.com/s/11h3Q6tsDtjQKTjUu3sc5cA?pwd=xjs9
- 夸克网盘: https://pan.quark.cn/s/3ee3d991d64b

모델 다운로드 후 압축을 풀고, 전체 디렉토리를 `.\MoneyPrinterTurbo\models`에 넣으세요.
최종 파일 경로는 다음과 같아야 합니다: `.\MoneyPrinterTurbo\models\whisper-large-v3`

```
MoneyPrinterTurbo
  ├─models
  │   └─whisper-large-v3
  │          config.json
  │          model.bin
  │          preprocessor_config.json
  │          tokenizer.json
  │          vocabulary.json
```

## 배경 음악 🎵

비디오의 배경 음악은 프로젝트의 `resource/songs` 디렉토리에 있습니다.
> 현재 프로젝트에는 YouTube 비디오에서 가져온 기본 음악이 일부 포함되어 있으며, 저작권 문제가 있는 경우 삭제하시기 바랍니다.

## 자막 폰트 🅰

비디오 자막 렌더링에 사용되며, 프로젝트의 `resource/fonts` 디렉토리에 있습니다. 자신의 폰트를 추가할 수도 있습니다.

## 자주 묻는 질문 🤔

### ❓RuntimeError: No ffmpeg exe could be found

일반적으로 ffmpeg는 자동으로 다운로드되고 자동으로 감지됩니다.
하지만 환경에 문제가 있어 자동 다운로드가 불가능한 경우 다음과 같은 오류가 발생할 수 있습니다:

```
RuntimeError: No ffmpeg exe could be found.
Install ffmpeg on your system, or set the IMAGEIO_FFMPEG_EXE environment variable.
```

이 경우 https://www.gyan.dev/ffmpeg/builds/ 에서 ffmpeg를 다운로드하고, 압축 해제 후 `ffmpeg_path`를 실제 설치 경로로 설정하세요.

```toml
[app]
# 실제 경로에 맞게 설정하세요. Windows 경로 구분자는 \\입니다
ffmpeg_path = "C:\\Users\\harry\\Downloads\\ffmpeg.exe"
```

### ❓ImageMagick의 보안 정책이 임시 파일@/tmp/tmpur5hyyto.txt와 관련된 작업을 차단합니다

이러한 정책은 ImageMagick의 설정 파일 policy.xml에서 찾을 수 있습니다.
이 파일은 일반적으로 /etc/ImageMagick-`X`/ 또는 ImageMagick 설치 디렉토리의 유사한 위치에 있습니다.
`pattern="@"`가 포함된 항목을 수정하여 `rights="none"`을 `rights="read|write"`로 변경하여 파일 읽기/쓰기 작업을 허용하세요.

### ❓OSError: [Errno 24] Too many open files

이 문제는 시스템의 열린 파일 수 제한으로 인해 발생하며, 시스템의 파일 열기 수 제한을 수정하여 해결할 수 있습니다.

현재 제한 확인

```shell
ulimit -n
```

너무 낮으면 높일 수 있습니다, 예:

```shell
ulimit -n 10240
```

### ❓Whisper 모델 다운로드 실패, 다음 오류 발생

LocalEntryNotfoundEror: Cannot find an appropriate cached snapshotfolderfor the specified revision on the local disk and
outgoing trafic has been disabled.
To enablerepo look-ups and downloads online, pass 'local files only=False' as input.

또는

An error occured while synchronizing the model Systran/faster-whisper-large-v3 from the Hugging Face Hub:
An error happened while trying to locate the files on the Hub and we cannot find the appropriate snapshot folder for the
specified revision on the local disk. Please check your internet connection and try again.
Trying to load the model directly from the local cache, if it exists.

해결 방법: [클릭하여 온라인 디스크에서 모델을 수동으로 다운로드하는 방법 보기](#자막-생성-)

## 피드백 및 제안 📢

- [issue](https://github.com/harry0703/MoneyPrinterTurbo/issues) 또는 [pull request](https://github.com/harry0703/MoneyPrinterTurbo/pulls)를 제출할 수 있습니다.

## 라이선스 📝

[`LICENSE`](LICENSE) 파일을 참조하세요

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=harry0703/MoneyPrinterTurbo&type=Date)](https://star-history.com/#harry0703/MoneyPrinterTurbo&Date)
