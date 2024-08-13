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


@app.route("/api-location")
def location_data():
    api_key = os.environ.get("OPEN_WEATHER_API_KEY")
    city_name = request.args.get("city_name") 
    location_data_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={api_key}"
    location_data_response = requests.get(location_data_url)
    location_data = location_data_response.json()
    return location_data

