import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import sys
import os
import re
import json
import time
import datetime

from flask import Flask
from flask import request
from flask import make_response
from flask import jsonify

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Hello World!'

@app.route('/keyboard')
def Keyboard():
    dataSend = {
        "type" : "buttons",
        "buttons" : ["시작하기"]
    }
    return jsonify(dataSend)

@app.route('/message', methods=['POST'])
def Message():
    dataReceive = request.get_json()
    content = dataReceive['content']

    if content == u"시작하
