import os
import json
from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')

youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    def __init__(self, channel_id: str) -> None:
        self.channel_id = channel_id

    def print_info(self) -> None:
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        channel_info = json.dumps(channel, indent=2, ensure_ascii=False)
        print(channel_info)