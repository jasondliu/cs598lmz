import ctypes
import ctypes.util
import threading
import sqlite3

from flask import Flask, Response, send_from_directory
from flask_socketio import SocketIO, emit
from flask_cors import CORS

from logger import logdecorator, logformatter

from eeg_pyaudio import Recording
from eeg_pyaudio import Recording2
from test_audio import Recording3
from eeg_pyaudio import Recording4

from functions import *
from yin import *
from link import *
from online import *

from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__, static_url_path='/static')
CORS(app)
socketio = SocketIO(app)

RECORDING = False

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/js/<path:path>")
def send_js(path):
    return send_from_directory("js", path)
