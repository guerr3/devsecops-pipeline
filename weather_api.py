# weather_api.py

from flask import Flask, jsonify, request
import os
import requests

app = Flask(__name__)

# Opzettelijk "lek" van API key (dit zal de secret detection triggeren)
WEATHER_API_KEY = "ab12cd34ef56gh78ij90kl12mn34op56"

# Onveilige configuratie (dit zal SAST triggeren)
app.config['DEBUG'] = True

@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    # Onveilige string formatting (dit zal SAST triggeren)
    query = "SELECT * FROM weather WHERE city = '%s'" % city
    
    # Simuleer een API call
    weather_data = {
        "city": city,
        "temperature": 20,
        "condition": "sunny"
    }
    
    return jsonify(weather_data)

@app.route('/admin', methods=['POST'])
def admin_panel():
    # Onveilige eval gebruik (dit zal SAST triggeren)
    command = request.json.get('command')
    result = eval(command)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)