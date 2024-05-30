import googlemaps

api_key = "AIzaSyCkpFwDSX_aIeOsgBb0emR0UZ9wITAylrc"
gmaps = googlemaps.Client(key=api_key)

start_point = "Your Start Location"
distance_km = 3

# Calculate a route to cover the specified distance and return to the start point
directions_result = gmaps.directions(
    start_point,
    start_point,
    mode="walking",  # You can adjust the mode based on your preference (e.g., "driving", "walking", "bicycling")
    waypoints=[],
    optimize_waypoints=True,
    units="metric",
    region="your_region"
)

# Extract and print the route steps
for step in directions_result[0]['legs'][0]['steps']:
    print(step['html_instructions'])