from flask_app import app
from flask import render_template, request, session

@app.route('/')
def main():
    return render_template('index.html')