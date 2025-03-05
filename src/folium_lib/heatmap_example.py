import folium
from folium import plugins
import numpy as np
import os

# 서울 중심 좌표
seoul_center = [37.5665, 126.9780]

# 기본 맵 생성
m = folium.Map(location=seoul_center, zoom_start=11)

# 샘플 데이터 생성 (100개의 임의 위치)
data = []
for i in range(100):
    lat = np.random.uniform(37.5, 37.6)
    lon = np.random.uniform(126.9, 127.0)
    data.append([lat, lon])

# 히트맵 레이어 추가
plugins.HeatMap(data).add_to(m)

# 맵 저장
m.save(os.path.join('data', 'heatmap_example.html'))