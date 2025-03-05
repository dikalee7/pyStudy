from PIL import Image
import requests
from io import BytesIO

def add_watermark(main_img_url, logo_url, output_path):
  # 메인 이미지 다운로드
  response = requests.get(main_img_url)
  main_img = Image.open(BytesIO(response.content))
  
  # 로고 이미지 다운로드
  response = requests.get(logo_url)
  logo = Image.open(BytesIO(response.content))
  
  # 메인 이미지 크기
  main_width, main_height = main_img.size
  
  # 로고 크기 계산 (메인 이미지의 20%)
  logo_width = int(main_width * 0.2)
  logo_height = int(main_height * 0.2)
  
  # 로고 리사이즈
  logo = logo.resize((logo_width, logo_height), Image.Resampling.LANCZOS)
  
  # 로고 위치 계산 (우측 하단)
  position = (main_width - logo_width - 10, main_height - logo_height - 10)
  
  # 로고에 알파 채널이 없다면 추가
  if logo.mode != 'RGBA':
    logo = logo.convert('RGBA')
  
  # 메인 이미지에 로고 합성
  main_img.paste(logo, position, logo)
  
  # 결과 저장
  main_img.save(output_path)
  
  # 결과 이미지 화면에 표시
  main_img.show()
# 사용 예시
main_image_url = "https://picsum.photos/400/200?random=1"
logo_url = "https://picsum.photos/400/200?random=2"
output_path = "output_images/output_watermarked.png"

add_watermark(main_image_url, logo_url, output_path)
