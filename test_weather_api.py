# test_weather_api.py

import unittest
from weather_api import app

class TestWeatherAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_weather(self):
        response = self.app.get('/weather/Amsterdam')
        self.assertEqual(response.status_code, 200)
        self.assertIn('temperature', response.json)

if __name__ == '__main__':
    unittest.main()