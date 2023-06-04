# Создайте файл video.py в папке src и поместите в него следующий код

class Video:
    def __init__(self, video_id):
        # Инициализация атрибутов экземпляра класса Video
        self.id = video_id
        self.title = "GIL в Python: зачем он нужен и как с этим жить"
        self.link = "https://www.youtube.com/watch?v=AWX4JnAnjBE"
        self.views = 1000
        self.likes = 50

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        # Инициализация атрибутов экземпляра класса PLVideo
        self.playlist_id = playlist_id
        self.title = 'MoscowPython Meetup 78 - вступление'





