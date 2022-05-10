import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H'), daemon=True).start()

# Import the necessary packages
import cv2
import os
import numpy as np
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import time
import datetime
import argparse
import json
from flask import Flask, render_template, Response
from flask import request
import time
from flask import Flask
from flask_socketio import SocketIO
import base64

# App config.
DEBUG = False
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Define the video stream
vs = VideoStream(src=0).start()
# Allow the camera or video file to warm up
time.sleep(2.0)

# Define the codec and create VideoWriter object
