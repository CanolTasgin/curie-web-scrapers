import requests
import json

# API key for Google Maps Places API
api_key = "_"

# Search for events related to "mental health" within a 5km radius of a given location
topic = "woman in science"
location = "40.748817,-73.985428"
radius = 500000  # in meters
url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={api_key}&location={location}&radius={radius}&keyword={topic}"

response = requests.get(url)
data = response.json()

# Extract the details of the events
events = []
for event in data['results']:
    events.append({
        'name': event['name'],
        'address': event['vicinity'],
        'opening_hours': event['opening_hours']['open_now'] if 'opening_hours' in event else None,
        'user_ratings_total': event['user_ratings_total'],
        'rating': event['rating']
    })

for event in events:
    print(event)

# Save the details of the events to a JSON file
with open("/Users/canoltasgin/Desktop/UofTHacks/CURIE/Backend/events.json", "w") as outfile:
    json.dump(events, outfile)
