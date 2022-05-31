from flask_app import app
from flask import render_template, request, jsonify, redirect, url_for
import os
import requests
import datetime

@app.route('/')
def main():
    r = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={os.environ.get('FLASK_APP_API_KEY')}&q=London&days=3&aqi=no&alerts=no")
    if r.status_code == 200:
        return render_template('index.html', data=r.json())
    return redirect(f"/error/{r.status_code}")

@app.route('/error/<int:code>')
def error(code):
    return f"<h1>Status Code:{code}</h1>"