from flask_app import app
from flask import render_template, request, jsonify, redirect, url_for
import os
import requests
import datetime

@app.route('/')
def main():
    r = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={os.environ.get('FLASK_APP_API_KEY')}&q=London&days=3&aqi=no&alerts=no")
    if r.status_code == 200:
        # for inx, x in enumerate(r.json()["forecast"]["forecastday"]):
        #     r.json()["forecast"]["forecastday"][inx]["date"] = datetime.datetime.strptime(x["date"], "%Y-%m-%d").strftime("%d %b, %Y")
        #     print(datetime.datetime.strptime(x["date"], "%Y-%m-%d").strftime("%d %b, %Y"))
        #     print(r.json()["forecast"]["forecastday"][inx]["date"])
        date = list(map(lambda x: datetime.datetime.strptime(x["date"], "%Y-%m-%d").strftime("%b %d, %Y"), r.json()["forecast"]["forecastday"]))
        # print(val)
        # print(r.json())
        return render_template('index.html', data=r.json(), date=date)
    return redirect(f"/error/{r.status_code}")

@app.route('/error/<int:code>')
def error(code):
    return f"<h1>Status Code:{code}</h1>"