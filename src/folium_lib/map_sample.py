import folium
import pandas as pd

# 서울시 주요 관광지 데이터
locations = {
    '명소': ['경복궁', '남산서울타워', '롯데월드', '동대문디자인플라자', '창덕궁'],
    '위도': [37.579617, 37.551168, 37.511390, 37.567255, 37.579389],
    '경도': [126.977041, 126.988194, 127.098209, 127.009467, 126.991389]
}

# DataFrame 생성
df = pd.DataFrame(locations)

# 서울 중심부 좌표로 지도 생성
seoul_map = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

# 관광지 마커 추가
for idx, row in df.iterrows():
    folium.Marker(
        location=[row['위도'], row['경도']],
        popup=row['명소'],
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(seoul_map)

# 지도 저장
seoul_map.save('seoul_tourist_spots.html')
