import os

# 현재 작업 디렉토리 확인
current_dir = os.getcwd()
print(f"현재 디렉토리: {current_dir}")

# 새 디렉토리 생성
os.makedirs("new_folder", exist_ok=True)

# 파일 목록 조회
directory = ".\\src"
files = os.listdir(directory)
print(f"파일 목록: {files}")
file_path = os.path.join(directory, files[0])
print(f"파일 명: {file_path}")

# 파일 존재 여부 확인
if os.path.exists("test.txt"):
    print("파일이 존재합니다")

# 파일 정보 확인
file_stat = os.stat("D:\pyAutoWork\src\sp_operations.py")
print(f"파일 크기: {file_stat.st_size} bytes")

# 환경 변수 접근
python_path = os.getenv("PYTHONPATH")
print(f"PYTHONPATH: {python_path}")

# 경로 결합
new_path = os.path.join(current_dir, "new_folder", "test.txt")
print(f"새 경로: {new_path}")

# 파일 이름과 확장자 분리
filename, ext = os.path.splitext("example.txt")
print(f"파일명: {filename}, 확장자: {ext}")

# 디렉토리 변경
os.chdir("new_folder")
print(f"변경된 디렉토리: {os.getcwd()}")
