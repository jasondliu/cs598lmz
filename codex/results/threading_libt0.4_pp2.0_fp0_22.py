import threading
threading.stack_size(67108864)

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from flask import render_template
from flask import send_from_directory
import time
import json

app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)

@app.route('/fonts/<path:path>')

