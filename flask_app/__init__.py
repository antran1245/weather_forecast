from flask import Flask
app = Flask(__name__)
app.secret_key = "weather"

from flask_app.controllers import weathers