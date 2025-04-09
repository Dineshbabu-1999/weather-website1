from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import requests  # Make sure to import the requests module

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# OpenWeatherMap API key (replace with your real API key)
API_KEY = "e0b54473564a741a5b28caa8722967d1"
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"  # Correct API URL

@app.route("/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city")

    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    try:
        # Fetch weather data from OpenWeatherMap API
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(WEATHER_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            return jsonify({"error": data.get("message", "Error fetching weather")}), 400

        weather_info = {
            "city": city,
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"]
        }
        return jsonify(weather_info)
    except Exception as e:
        return jsonify({"error": "Something went wrong"}), 500

if __name__ == "__main__":
    app.run(debug=True)
