from app import app
from flask import jsonify, request
import os
import requests

@app.route("/")
def index():
    return "Hello World!"

"""@app.route("/open-weather-api")
def open_weather_api():
    api_key = os.environ.get("OPEN_WEATHER_API_KEY")
    return jsonify({"api_key": api_key})"""

@app.route("/test")
def test():
    return "test"

@app.route("/api-location")
def location_data():
    api_key = os.environ.get("OPEN_WEATHER_API_KEY")
    city_name = request.args.get("city_name") 
    location_data_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={api_key}"
    location_data_response = requests.get(location_data_url)
    location_data = location_data_response.json()
    return location_data

@app.route("/api-weather")
def weather_data():
    api_key = os.environ.get("OPEN_WEATHER_API_KEY")
    longitude = request.args.get("lon")
    latitude = request.args.get("lat")
    city_name = request.args.get("city_name")
    weather_data_url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
    weather_data_response = requests.get(weather_data_url)
    weather_data_json = weather_data_response.json()
    #print(weather_data_json)
    clouds = weather_data_json["clouds"]["all"]
    if (clouds == 100):
        clouds = "Cloudy"
    elif (clouds > 50):
        clouds = "Mostly cloudy"
    else:
        clouds="Partly cloudy"

    weather_data = {"city_name": city_name, "temperature": round(weather_data_json["main"]["temp"]),
                    "feels_like": round(weather_data_json["main"]["feels_like"]),
                    "clouds": clouds}
    return jsonify(weather_data)
