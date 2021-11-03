from flask import Flask

import smtplib



app = Flask(__name__)

@app.route("/")
def index():
    return "Sent"

