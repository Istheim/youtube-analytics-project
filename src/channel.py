import os
import requests
import json


class Channel:
    def __init__(self, channel_id):
        self.channel_id = channel_id

    def print_info(self):
        api_key = os.getenv("YT_API_KEY")
        url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={self.channel_id}&key={api_key}"
        response = requests.get(url)
        data = json.loads(response.text)

        if "items" in data and len(data["items"]) > 0:
            channel = data["items"][0]
            snippet = channel["snippet"]
            statistics = channel["statistics"]

            print(f"Title: {snippet['title']}")
            print(f"Description: {snippet['description']}")
            print(f"Custom URL: {snippet['customUrl']}")
            print(f"Published At: {snippet['publishedAt']}")
            print(f"View Count: {statistics['viewCount']}")
            print(f"Subscriber Count: {statistics['subscriberCount']}")
            print(f"Video Count: {statistics['videoCount']}")
        else:
            print("Channel not found")

