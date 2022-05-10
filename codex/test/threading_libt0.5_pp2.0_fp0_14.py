import threading
threading.stack_size(67108864)

import os
import sys
import json
import time
import logging
import random
import requests
import datetime

from flask import Flask, request
from flask_cors import CORS

from common import *

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/get_all_users')
def get_all_users():
    return get_all_users_from_db()

@app.route('/get_user_by_username', methods=['POST'])
def get_user_by_username():
    data = request.get_json()
    username = data['username']
    return get_user_by_username_from_db(username)

@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data['username']
    password = data['password']
