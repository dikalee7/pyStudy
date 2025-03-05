from PIL import Image, ImageEnhance
import os

def process_images(input_folder, output_folder):
    # 출력 폴더가 없으면 생성
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 입력 폴더의 모든 이미지 파일 처리
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            # 이미지 열기
            image_path = os.path.join(input_folder, filename)
            img = Image.open(image_path)
            
            # 이미지 처리
            # 1. 밝기 향상
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(1.2)
            
            # 2. 대비 향상
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(1.1)
            
            # 3. 크기 조정 (50% 축소)
            width, height = img.size
            img = img.resize((width // 2, height // 2))
            
            # 처리된 이미지 저장
            output_path = os.path.join(output_folder, f'processed_{filename}')
            img.save(output_path)

if __name__ == '__main__':
    input_folder = 'input_images'
    output_folder = 'output_images'
    process_images(input_folder, output_folder)
