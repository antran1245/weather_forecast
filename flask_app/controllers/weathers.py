from flask_app import app
from flask import render_template, request, jsonify, redirect
import os
import requests

@app.route('/')
def main():
    # r = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={os.environ.get('FLASK_APP_API_KEY')}&q=London&days=3&aqi=no&alerts=no")
    # if r.status_code == 200:
    # print(r.json())
    return redirect('/forcast')

@app.route('/forcast')
def forcast():
    return render_template('index.html')