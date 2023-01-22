import requests
import json

# specify the topic, NewsAPI key, and number of results to retrieve
topic = "machine learning"
api_key = "_"
num_results = 10

# create the NewsAPI URL
url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}&pageSize={num_results}"

# make the request
response = requests.get(url)
# parse the response
data = response.json()
# get the list of articles
articles = data["articles"]

with open("/Users/canoltasgin/Desktop/UofTHacks/CURIE/Backend/news.json", "w") as outfile:
    json.dump(articles, outfile)
