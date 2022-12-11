import requests
from src import settings


class WeatherApiClient(object):

    def __init__(self):
        self.api_key = settings.api_key
        self.url = settings.api_url

    def get_current_weather(self):
        pass

    def get_tomorrow_weather(self):
        pass

    def get_yesterday_weather(self):
        pass