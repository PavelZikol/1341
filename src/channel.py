import json
import os
from googleapiclient.discovery import build


YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
class Channel:
    """Класс для ютуб - канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала.
        Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel_info = self.get_channel_info()
        self.title = self.channel_info["items"][0]["snippet"]["title"]
        self.desc = self.channel_info["items"][0]["snippet"]["description"]
        self.url = "https://www.youtube.com/" + self.channel_info["items"][0]["snippet"][
            "customUrl"]
        self.channel_subs_count = self.channel_info["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.channel_info["items"][0]["statistics"]["videoCount"]
        self.channel_views = self.channel_info["items"][0]["statistics"]["viewCount"]

    def get_channel_info(self):
        """Получение информации о канале"""
        channel = self.get_service().channels().list(id=self.__channel_id,
                                                     part="snippet,statistics").execute()
        return channel

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.get_service().channels().list(id=self.channel_id,
                                                     part="snippet,statistics").execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    def to_json(self, json_name):
        """Инфа о канале в Json"""
        data = {"channel_id": self.channel_id,
                "channel_title": self.title,
                "channel_description": self.desc,
                "channel_url": self.url,
                "channel_count_subscribe": self.channel_subs_count,
                "channel_count_video": self.video_count,
                "channel_views": self.channel_views}
        with open(json_name, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    @property
    def channel_id(self):
        """айди канала"""
        return self.__channel_id
1
    @classmethod
    def get_service(cls):
        """Получение информации о сервисе"""
        website = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
        return website
