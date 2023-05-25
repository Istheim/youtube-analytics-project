import os
import json
from googleapiclient.discovery import build

api_key = os.getenv('YT_API_KEY')

youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    def __init__(self, channel_id: str):
        self.__channel_id = channel_id
        self.title = ''
        self.description = ''
        self.url = ''
        self.subscriber_count = 0
        self.video_count = 0
        self.view_count = 0
        self.fill_channel_data()

    @property
    def channel_id(self):
        return self.__channel_id

    def fill_channel_data(self):
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        channel_snippet = channel['items'][0]['snippet']
        channel_statistics = channel['items'][0]['statistics']

        self.title = channel_snippet['title']
        self.description = channel_snippet['description']
        self.url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self.subscriber_count = int(channel_statistics['subscriberCount'])
        self.video_count = int(channel_statistics['videoCount'])
        self.view_count = int(channel_statistics['viewCount'])

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        return self.subscriber_count - other.subscriber_count

    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count

    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        return self.subscriber_count <= other.subscriber_count

    def __eq__(self, other):
        return self.subscriber_count == other.subscriber_count








