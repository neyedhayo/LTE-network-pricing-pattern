import numpy as np
from geopy.distance import geodesic
from geopy.point import Point

def haversine(lon1, lat1, lon2, lat2):
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

# cork, Ireland coordinate
lon1, lat1 = 8.473233, 51.898205 #  T12 EK53, Centre, Cork, Ireland
lon2, lat2 = -8.489030, 51.893012 # University College Cork, College Rd, University College, Cork, Ireland
distance_ireland = haversine(lon1, lat1, lon2, lat2)

# print(f"Distance between the Cork location: {distance_ireland: .2f} km\n")
# Start point in Lagos (around Broad St, Lagos Island, Lagos 102273, Lagos)
start_point = Point(6.454093971758886, 3.3892800580380427)

# Corrected distance (approx. 2 km)
correct_distance_km = 2.4

# Calculate the stop point using the geodesic distance calculation method
bearing_degrees = 90  # Eastward direction
correct_stop_point = geodesic(kilometers=correct_distance_km).destination(start_point, bearing_degrees)

# Print calculated values with 7 decimal places
print(f"Start point in Lagos: ({start_point.latitude:.7f}, {start_point.longitude: .16f})")
print(f"Stop point in Lagos approximating same distance: ({correct_stop_point.latitude:.16f}, {correct_stop_point.longitude:.7f})") # Dolphine Estate, Lagos 106104, Lagos

lagos_start_lat = start_point.latitude
lagos_start_lon = start_point.longitude
lagos_stop_lat = correct_stop_point.latitude
lagos_stop_lon = correct_stop_point.longitude

# Generate linear data points between the start and stop points in Lagos
num_points = 910
lons = np.linspace(lagos_start_lon, lagos_stop_lon, num_points)
lats = np.linspace(lagos_start_lat, lagos_stop_lat, num_points)

# Convert zip to list before slicing to avoid TypeError
lon_lat_pairs = list(zip(lons, lats))
for lon, lat in lon_lat_pairs[:1]:  # Print first 5 for brevity
    print(f"(Latitude, Longitude): {lat}, {lon}")

