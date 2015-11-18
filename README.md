# launch-scrubber-kata
Code exercise (in Python) for mocking an external service. Is the rocket launch a Go or No-Go? Depends on the weather.

## Problem Statement

Write a tool that determines whether or not to scrub today's launch.

1. Scrub the launch if the temperature is below 2 °C
2. Scrub the launch if the wind speed is above 37 km/h.
3. Scrub the launch if the temperature is below 9 °C and the wind speed is below 16 km/h.

## Setup

 - Python 3: `brew install python3`
 - Nose test runner: `pip3 install nose`

## Get Started

Run the tests with `nosetests`. See [tests/launch_scrubber_test.py]() to get started.

## WeatherStation

There is a `WeatherStation` object available that provides the following interface:

```python
from app import WeatherStation

station = WeatherStation()
temp = station.current_temperature # => 23.1 (Celsius)
wind = station.current_wind_speed # => 30.2 (km/h)

```
