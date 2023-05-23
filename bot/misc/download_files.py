import os

from pytube import YouTube
import ssl


class Video:
    def __init__(self, link):
        ssl._create_default_https_context = ssl._create_stdlib_context
        self.link = link
        self.youtube = YouTube(link)

    @property
    def autor(self):
        return self.youtube.author

    @property
    def name(self):
        name = self.youtube.title if '/' not in self.youtube.title else self.youtube.title.replace('/', '\\')
        return name

    @property
    def length(self):
        return self.youtube.length

    def download_audio(self):
        self.youtube.streams.get_audio_only().download(filename=self.name + ".mp3")

    def delete_audio(self):
        path = f'{self.name + ".mp3"}'
        if os.path.exists(path):
            os.remove(path)
