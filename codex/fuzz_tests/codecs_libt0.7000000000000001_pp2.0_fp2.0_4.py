import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import logging
import logging.handlers
import time
import json
import random
import traceback
import pymysql
import pymysql.cursors
import configparser
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.gen
import redis
import requests
import datetime
from tornado.options import define, options
from itertools import *
from pymongo import MongoClient
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor

from flask import Flask
from flask import request
from flask import jsonify

logger = logging.getLogger()

executor = ThreadPoolExecutor(4)

app = Flask(__name__)

conn = MongoClient("localhost", 27017)
db = conn.test
collection = db.test_collection 

@app.route("/mongotest", methods
