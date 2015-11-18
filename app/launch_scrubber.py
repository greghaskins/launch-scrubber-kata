from .external import WeatherStation

class Scrubber:

    def __init__(self):
        self.weather_station = WeatherStation()

    def go_for_launch(self):
        return True
