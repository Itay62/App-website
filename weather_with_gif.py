from flask import Flask, render_template
from settings import open_weather_token, giphy_token
import requests
app = Flask(__name__, template_folder='templateFiles',
            static_folder='staticFiles')


@app.route('/')
def hello():
    return render_template('main.html')


@app.route('/weather/<city>')
def weather(city):
    open_weather_url = "https://api.openweathermap.org/data/2.5/weather"
    open_weather_params = {'q': city,
                           'units': 'metric', 'appid': open_weather_token}
    open_weather_response = requests.get(
        url=open_weather_url, params=open_weather_params)
    temp = open_weather_response.json()['main']['temp']
    giphy_url = "https://api.giphy.com/v1/gifs/translate"
    giphy_params = {}
    search_word = ""
    if temp > 25:
        search_word = 'spicy weather'
    elif temp > 15:
        search_word = 'i love it'
    else:
        search_word = 'stay home'
    giphy_params = {'api_key': giphy_token,
                    's': search_word}
    giphy_response = requests.get(url=giphy_url, params=giphy_params)
    gif = giphy_response.json()['data']['images']['original']['url']
    return f'Hello {city}! it is {str(temp)} <img src={gif}>'


if __name__ == "__main__":
    app.run()
