import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 0)


import json
import os 
import uuid
from flask import Flask, request, redirect, g, render_template, session, send_from_directory
from flask_api import status
from werkzeug.utils import secure_filename
from scripts import image_recognition
import mysql.connector
import pandas as pd
import keras
from keras.models import model_from_json
import keras.backend as K

# ***** Initialization ***** #

# Slim API version
API_VERSION = "a"

# Flask boilerplate
application = app = Flask(__name__)

# Dictionary where you can register which 
# methods are allowed to be called through API
allowable_methods = {
    "images": ["POST", "GET"]
}

# ***** Function definitions ***** #

# Helper method to determine if the request is valid and if the content type is appropriate
def validate_request(content_type):
    return content_type and allowed_file(
