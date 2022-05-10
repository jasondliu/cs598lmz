import threading
threading.stack_size(500000000)

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_socketio import send, emit

import json
import time
import os
import sys

from pymongo import MongoClient
from bson import json_util
from bson.objectid import ObjectId

from helper import *


# Create the application instance
app = Flask(__name__, template_folder="templates")
CORS(app)

# Create the Socket.IO instance
socketio = SocketIO(app, cors_allowed_origins="*")

# Create a MongoDB client
client = MongoClient('localhost', 27017)

# Connect to the database
db = client.mms


@app.route('/')
def home():
    return render_template('index.html')


@socketio.on('connect')
def handle_connect():
    """
    Handle connection event
    """
    print('Client connected')


