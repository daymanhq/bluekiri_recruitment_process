import unittest
from web_app import city_weather

class TestStringMethods(unittest.TestCase):

    def test_city_weather(self):
        city = 'Palma'
        data = ' "city": "{}",\n    "temperature":'.format(city)
        self.assertIn(data, city_weather(city))

if __name__ == '__main__':
    unittest.main()