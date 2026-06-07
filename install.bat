@echo off
echo 파이썬 설치 확인 중...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 파이썬이 설치되어 있지 않습니다.
    echo https://www.python.org/downloads/ 에서 파이썬을 설치하세요.
    pause
    exit
)
echo 파이썬 확인 완료.
echo openpyxl 설치 중...
pip install openpyxl
echo 설치 완료. 이제 abc_plus.bat 을 실행하세요.
pause
