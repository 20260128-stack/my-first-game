# Week 11 실습
## 오늘 한 것
- PyInstaller 설치 및 빌드
- resource_path() 함수 추가
- --add-data 옵션으로 에셋 포함
- .exe 실행 확인
## 빌드 명령어
- `pyinstaller --version`
- `pyinstaller game.py`
- `dir`
- `pyinstaller main.py`
- `pyinstaller --onefile --windowed game.py`
## AI 활용 내역
- Thonny에서 `pyinstaller --version` 실행 시 발생한 오류 원인 설명 받음
- `pyinstaller --version`은 파이썬 코드가 아니라 터미널 명령어라는 설명 받음
- `NameError: name 'pyinstaller' is not defined` 오류 원인 설명 받음
- PyInstaller 설치 여부 확인 방법 안내 받음
- Thonny의 "시스템 쉘 열기"가 CMD와 유사한 환경이라는 설명 받음
- `ERROR: Script file 'game.py' does not exist.` 오류 원인 설명 받음
- 현재 폴더에 `game.py` 파일이 존재해야 한다는 설명 받음
- `dir` 명령어로 파일 존재 여부 확인 방법 안내 받음
- 파일명이 `main.py`일 가능성 및 저장 위치 문제 설명 받음
- `pyinstaller main.py` 방식으로 실행 가능하다는 안내 받음
- `--onefile`, `--windowed` 옵션의 기능 설명 받음
- 빌드 완료 후 `dist` 폴더에 exe 파일 생성된다는 설명 받음
## resource_path() 를 써야 하는 이유
- 이미지 에셋, 혹은 오디오 파일 같이, 개발자의 개인 파일에만 존재하는 것들이 들어가있는 게임 파일의 경우,
.exe 파일로 공유를 하였을 때 게임이 정상적으로 실행되지 않거나 깨져보일 수 있다,
resource_path()를 사용하여 정상적으로 작동되게 한다. 즉 정상적인 게임의 작동과 유저의 편의를 위하여
resource_path()를 사용함으로서 내 게임이 담긴 .exe 파일을 유저에게 정상적으로 공유해야한다.
