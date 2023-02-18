from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    url ='https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/London,UK/2020-12-15T13:00:00'
    key = request.args.get('key')
    params = {'key': key}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return 'Error fetching weather data', 500

if __name__ == '__main__':
    app.run(debug=True)