from flask import Flask
from flask_restful import Resource, Api
import requests
import pytemperature

app = Flask(__name__)
api = Api(app)

apikey = '7f19c483f79021245b5828b1764205ee'


class CityWeather(Resource):

	def get(self, name_city):
		weather_api = 'https://api.openweathermap.org/data/2.5/weather?q={}&'\
		'appid={}'.format(name_city, apikey)
		result = requests.get(weather_api)
		
		data_weather =  result.json()
		main = data_weather["main"]
		temperature = main["temp"]
		temperature_celsius = pytemperature.k2c(temperature)

		return {
			"city": name_city,
			"temperature": temperature_celsius
		}

api.add_resource(CityWeather, '/city_weather/<name_city>')



if __name__ == '__main__':
	app.run(debug=True)
		