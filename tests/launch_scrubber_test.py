import unittest

from app.launch_scrubber import Scrubber

class LaunchScrubberTests(unittest.TestCase):

    def setUp(self):
        self.scrubber = Scrubber()

    def test_launch_is_scrubbed_when_its_too_cold(self):
        # ...
        self.assertFalse(self.scrubber.go_for_launch())

    def test_launch_is_go_when_weather_looks_good(self):
        # ...
        self.assertTrue(self.scrubber.go_for_launch())

    def test_launch_is_no_go_when_its_too_windy(self):
        # ...
        self.assertFalse(self.scrubber.go_for_launch())

    def test_launch_is_no_go_if_not_warm_enough_on_calm_day(self):
        # ...
        self.assertFalse(self.scrubber.go_for_launch())


if __name__ == '__main__':
    unittest.main()
