import ctypes
import ctypes.util
import threading
import sqlite3
import json
import signal

from flask import Flask, render_template, send_from_directory, request
from flask_socketio import SocketIO, emit
from flask_cors import cross_origin

from settings import *

#thread = None

app = Flask(__name__, static_url_path='/static')
socketio = SocketIO(app)


# TODO:
# Fix clicking other buttons does not refresh page
# Fix clicking "stop" does not do anything
# Add logging to file



# ==================================================================================================
#
#       Functions
#
# ==================================================================================================

def get_ip():
    """
    Returns the ip of the computer that is running this script
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip



