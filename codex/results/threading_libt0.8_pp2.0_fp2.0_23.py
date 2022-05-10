import threading
threading.stack_size(2**27)
import sys

from flask import render_template
from flask import Flask
from application import app
from application import camera
from flask import make_response
from flask import Response
from flask import jsonify
from flask import request, redirect, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename
from application import model
from flask import send_from_directory
from PIL import Image
from application import log
import os
import io

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['UPLOAD_FOLDER'] = 'static/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])

#The ip address of your computer (or raspberry pi)
IP = "192.168.0.17"

#The port you want the server to be available on
PORT = "5000"

#This is used for communication between the webpage and the server
@app.route
