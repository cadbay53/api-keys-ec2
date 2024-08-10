from app import app
from flask import jsonify
import os

@app.route("/")
def index():
    return "Hello World!"

@app.route("/open-weather-api")
def open_weather_api():
    api_key = os.environ.get("OPEN_WEATHER_API_KEY")
    return jsonify({"api_key": api_key})
