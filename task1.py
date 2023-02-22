from flask import Flask, request
import requests
import datetime

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    url = 'http://api.openweathermap.org/data/2.5/weather'
    api_key = '96c9cdfd4ebba5f201652765b7290f2e'
    place = request.args.get('place')
    params = {'q': place, 'appid': api_key}
    response = requests.get(url, params=params)
if response.status_code == 200:
        return response.json()
    else:
        return 'Error fetching weather data', 500

if __name__ == '__main__':
    app.run(debug=True)
    
