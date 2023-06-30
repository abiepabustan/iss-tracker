import json
import time
import requests

data_points = []

for _ in range(100):
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    latitude = float(data['iss_position']['latitude'])
    longitude = float(data['iss_position']['longitude'])
    timestamp = data['timestamp']
    data_points.append((latitude, longitude, timestamp))
    time.sleep(10)

import matplotlib.pyplot as plt

latitudes = [point[0] for point in data_points]
longitudes = [point[1] for point in data_points]

plt.plot(longitudes, latitudes)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Path of the International Space Station')
plt.show()
