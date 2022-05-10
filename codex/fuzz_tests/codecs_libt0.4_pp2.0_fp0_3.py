import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import sys
import time
import json
import datetime
import pymysql
import logging
from logging.handlers import TimedRotatingFileHandler
from flask import Flask, request, abort, jsonify
from flask_cors import CORS

# Logging
logger = logging.getLogger('flask')
logger.setLevel(logging.DEBUG)
handler = TimedRotatingFileHandler('./log/flask.log', when='midnight')
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Flask
app = Flask(__name__)
CORS(app)

# MySQL
conn = pymysql.connect(host='localhost', user='root', password='', db='test', charset='utf8mb4')
curs
