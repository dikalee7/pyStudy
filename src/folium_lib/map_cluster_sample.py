import folium
from folium.plugins import MarkerCluster
import os

# Create base map centered on Seoul
map = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

# Create a MarkerCluster object
marker_cluster = MarkerCluster()

# Sample location data
locations = [
    {"name": "Seoul Station", "lat": 37.5546, "lon": 126.9706},
    {"name": "Gangnam Station", "lat": 37.4980, "lon": 127.0276},
    {"name": "Hongdae", "lat": 37.5565, "lon": 126.9242},
    {"name": "Jamsil", "lat": 37.5130, "lon": 127.0980},
    {"name": "Yeouido", "lat": 37.5219, "lon": 126.9242}
]

# Add markers to the cluster
for loc in locations:
    folium.Marker(
        location=[loc["lat"], loc["lon"]],
        popup=loc["name"],
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(marker_cluster)

# Add the marker cluster to the map
marker_cluster.add_to(map)

# Save the map
map.save(os.path.join('data', 'map_cluster_sample.html'))