import unittest
from api import CityWeather
import requests

class TestStringMethods(unittest.TestCase):
    global city, api_key, bad_api_key
    city = 'Palma'
    api_key = '7f19c483f79021245b5828b1764205ee'
    bad_api_key = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

    def test_openweathermap_api_connect(self):
        weather_api = 'https://api.openweathermap.org/data/2.5/weather?q={}&'\
        'appid={}'.format(city, api_key)
        
        result = requests.get(weather_api)
        self.assertTrue(result.ok)

    def test_openweathermap_api_bad_connection(self):
        weather_api = 'https://api.openweathermap.org/data/2.5/weather?q={}&'\
        'appid={}'.format(city, bad_api_key)
        
        result = requests.get(weather_api)
        self.assertFalse(result.ok)

    def test_my_api(self):
        cw = CityWeather()
        data = "{'city': '" + city + "', 'temperature':"

        self.assertIn(data, str(cw.get(city)))

if __name__ == '__main__':
    unittest.main()