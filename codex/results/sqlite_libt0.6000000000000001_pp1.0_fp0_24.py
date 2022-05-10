import ctypes
import ctypes.util
import threading
import sqlite3

from flask import Flask, g, request, jsonify
from flask_cors import CORS

import logger

app = Flask(__name__)
CORS(app)

# Load the libary
lib_path = ctypes.util.find_library("libgrpc++.so")
logger.info("Loaded libary: %s", lib_path)
lib = ctypes.cdll.LoadLibrary(lib_path)

# Setup the logger
logger.setup()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('db.sqlite')
    return db

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:

