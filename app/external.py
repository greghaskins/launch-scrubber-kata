import random

class WeatherStation:

    @property
    def current_temperature(self):
        return random.uniform(-3.1, 32.4)

    @property
    def current_wind_speed(self):
        return random.uniform(5.0, 50.0)
