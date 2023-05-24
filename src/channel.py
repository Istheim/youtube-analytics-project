import os
import os
import json
from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')

youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    def __init__(self, channel_id: str) -> None:
        self.channel_id = channel_id
        self.title = ''
        self.description = ''
        self.url = ''
        self.subscriber_count = 0
        self.video_count = 0
        self.view_count = 0
        self.fill_channel_data()

    def fill_channel_data(self) -> None:
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        channel_snippet = channel['items'][0]['snippet']
        channel_statistics = channel['items'][0]['statistics']

        self.title = channel_snippet['title']
        self.description = channel_snippet['description']
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscriber_count = int(channel_statistics['subscriberCount'])
        self.video_count = int(channel_statistics['videoCount'])
        self.view_count = int(channel_statistics['viewCount'])

    def print_info(self) -> None:
        channel_info = {
            'id': self.channel_id,
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

    def to_json(self, filename: str) -> None:
        channel_info = {
            'id': self.channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count
        }
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(channel_info, file, ensure_ascii=False, indent=2)



