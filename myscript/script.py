import sys
import requests

arguments = sys.argv

if len(arguments) > 2:
	print("\n Bad use. Pleas insert only 1 parameters. For cities with complex name, write with next separator: _ \n")
else:
	name_city = arguments[1].replace("_", " ") if "_" in arguments[1] else arguments[1]
	query_web = requests.get('http://0.0.0.0/dayman_weather/' + name_city)
	
	result = query_web.json()
	temp = int(result["temperature"])
	city = result["city"]

	print("\n Weather forecast for tomorrow in {} Temperature: {} ºC \n".format(city, temp))