# 🐾 Dog vs Cat Image Classifier

이 프로젝트는 사전 학습된 [Xception Deep Learning Model](https://keras.io/api/applications/xception/)을 활용하여 업로드 된 이미지가 **강아지**인지 **고양이**인지 분류해주는 웹 서비스입니다. 

사용자가 이미지를 업로드하면 웹상에서 해당 이미지를 실시간으로 전처리한 뒤, 모델의 예측값을 바탕으로 분류 결과와 신뢰도(Confidence) 퍼센테이지를 보여줍니다.

## 🚀 기술 스택
- **언어**: Python 3.11
- **프론트엔드/백엔드 서버**: [Streamlit](https://streamlit.io/)
- **딥러닝 프레임워크**: [TensorFlow (Keras)](https://www.tensorflow.org/)
- **이미지 처리**: Pillow (PIL), NumPy

## 📝 설치 및 실행 방법

> **Note**: 현재 macOS (Apple Silicon 칩) 환경에서는 최신 버전의 Python 3.13 과 TensorFlow 2.20 간에 치명적인 `libc++abi mutex lock` 멀티쓰레딩 충돌 버그가 존재합니다. 따라서 안정적인 구동을 위해 **Python 3.11 환경**에서 실행해야 합니다.

### 1. 가상 환경 설정 (Conda 권장)

기본 터미널을 열고 다음 명령어를 통해 Python 3.11 버전의 가상 환경(`tf-env`)을 만듭니다.

```bash
# 가상 환경 생성
conda create -n tf-env python=3.11 -y

# 가상 환경 활성화
conda activate tf-env
```

### 2. 패키지 설치

활성화된 가상 환경에서, 다음 명령어로 필요한 파이썬 라이브러리들을 설치합니다.

```bash
pip install -r requirements.txt
```

### 3. 애플리케이션 실행

설치가 완료되면, 다음 명령어로 Streamlit 웹 서버를 구동합니다.

```bash
streamlit run app.py
```

명령어가 성공적으로 실행되면 터미널에 `Local URL: http://localhost:8501` (또는 8502) 형식의 주소가 표시되며, 웹 브라우저가 자동으로 열립니다. 

만약 자동으로 열리지 않는다면, 브라우저 주소창에 `http://localhost:8501` (또는 사용된 포트 번호)를 직접 입력해 접속하시면 됩니다!

## 📂 주요 파일 설명
- `app.py`: 웹페이지 UI 구성 및 이미지 전처리, 모델 예측을 수행하는 메인 코드가 작성되어 있습니다.
- `requirements.txt`: 프로젝트 구동에 필요한 패키지(라이브러리) 목록이 정의되어 있습니다.
- `best_model_xception.keras`: 강아지와 고양이를 분류하도록 학습이 완료된 딥러닝 모델 파일입니다. **(용량이 약 90MB이므로 GitHub 업로드 시 `.gitignore`에 의하여 제외됩니다.)**
