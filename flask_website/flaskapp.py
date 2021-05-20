import base64
import datetime

import flask
from flask import (Flask, jsonify, render_template, request,
                   send_from_directory, make_response)

app = Flask(__name__)

import pytz
SG = pytz.timezone('Singapore')

@app.route('/')
def onboarding():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
