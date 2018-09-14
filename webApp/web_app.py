from flask import Flask, redirect
import requests

app = Flask(__name__)
 
@app.route('/dayman_weather/<name>')
def city_weather(name):
    info = requests.get('http://localhost:5000/city_weather/' + name)
    return info.text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)