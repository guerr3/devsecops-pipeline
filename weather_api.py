# weather_api.py

from flask import Flask, jsonify, request, abort
import os
import requests

app = Flask(__name__)

# Opzettelijk "lek" van API key (dit zal de secret detection triggeren)
WEATHER_API_KEY = "ab12cd34ef56gh78ij90kl12mn34op56"

# Schakel debug-modus uit voor productie
app.config['DEBUG'] = False

@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    # Gebruik parameterized queries om SQL-injectie te voorkomen
    # Voor deze demo wordt een dummy database-simulatie gebruikt
    weather_data = {
        "city": city,
        "temperature": 20,
        "condition": "sunny"
    }
    
    return jsonify(weather_data)
    

@app.route('/admin', methods=['POST'])
def admin_panel():
    # Verwijder onveilige eval-gebruik en implementeer veilige commando's
    command = request.json.get('command')
    if command not in ['status', 'restart', 'shutdown']:
        abort(403, description="Unauthorized command")

    # Simuleer veilige commando-uitvoering
    result = f"Executed command: {command}"
    return jsonify({"result": result})


if __name__ == '__main__':
    app.run(debug=True)