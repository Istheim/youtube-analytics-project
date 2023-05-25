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

    def print_info(self):
        channel_info = {
            'id': self.__channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count
        }
        channel_info_str = json.dumps(channel_info, indent=2, ensure_ascii=False)
        print(channel_info_str)

    @staticmethod
    def get_service():
        return youtube

    def to_json(self, filename: str):
        channel_info = {
            'id': self.__channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count
        }
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(channel_info, file, ensure_ascii=False, indent=2)







