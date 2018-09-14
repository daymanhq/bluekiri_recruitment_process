import sys
import requests

arguments = sys.argv

if len(arguments) > 2:
	print("bad use")
else:
	query_web = requests.get('http://0.0.0.0/dayman_weather/' + arguments[1])
	result = query_web.json()
	temp = int(result["temperature"])
	city = result["city"]

	print("\n Weather forecast for tomorrow in {} Temperature: {} ºC \n".format(city, temp))