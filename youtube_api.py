import requests
import json

# specify the keywords and YouTube Data API key
keywords = [
    "female scientist",
    "female engineers",
    "female researcher",
    "female physicist",
    "female mathematician",
    "female astronomer",
    "women in science",
    "women in technology",
    "women in engineering",
    "women in STEM",
    "girl in science",
    "girl in technology",
    "girl in engineering",
    "girl in STEM"]
api_key = "_"

# create an empty list to store the video details
videos = []

# loop through the keywords
for keyword in keywords:
    # create the search URL
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={keyword}&type=video&key={api_key}"
    # make the request
    response = requests.get(url)
    data = response.json()
    # loop through the videos in the response
    for item in data["items"]:
        # extract the video details
        link = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        title = item["snippet"]["title"]
        description = item["snippet"]["description"]
        # add the video details to the list
        videos.append({"link": link, "title": title,
                       "description": description})

# write the list of videos to a JSON file
with open("/Users/canoltasgin/Desktop/UofTHacks/CURIE/Backend/videos.json", "w") as f:
    json.dump(videos, f)
