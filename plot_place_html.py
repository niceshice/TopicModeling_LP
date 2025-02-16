import pandas as pd
import folium
from geopy.geocoders import Nominatim
from collections import Counter
import time
from folium.plugins import MarkerCluster

# Load CSV file
df = pd.read_csv("collection.csv")

# Ensure column name is correct
if "pub_place" not in df.columns:
    raise ValueError("The CSV file must have a 'pub_place' column.")

# List of place names
places = df["pub_place"].dropna().tolist()  # Drop missing values

# Manually correct known geocoding mistakes
manual_corrections = {
    "Brieg": "Brzeg, Poland"  # Fixes the incorrect placement in France
    ,"Ursel": "Oberursel, Germany" # Fixes the incorrect placement in Belgium
    ,"Oels": "Olesnica, Poland" # Fixes the incorrect placement in Czechia
}

# Apply corrections
places = [manual_corrections.get(place, place) for place in places]

# Count occurrences of each place
place_counts = Counter(places)

# Initialize geocoder
geolocator = Nominatim(user_agent="geo_mapping")

# Create a base map centered in Germany
germany_map = folium.Map(location=[51.1657, 10.4515], zoom_start=6)

# Use a MarkerCluster for better visualization
marker_cluster = MarkerCluster().add_to(germany_map)

# Convert place names to coordinates and add markers
for place, count in place_counts.items():
    try:
        location = geolocator.geocode(place)
        if location:
            folium.CircleMarker(
                location=[location.latitude, location.longitude],
                radius=5 + count,  # Adjust size based on frequency
                color="blue",
                fill=True,
                fill_color="blue",
                fill_opacity=0.6,
                popup=f"{place} ({count} occurrences)"
            ).add_to(marker_cluster)
        time.sleep(1)  # To avoid hitting rate limits
    except Exception as e:
        print(f"Error fetching {place}: {e}")

# Save and open map
germany_map.save("germany_map.html")
print("Map saved as germany_map.html. Open it in a browser.")
