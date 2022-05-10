import mmap
import json
import sys
import os
import datetime

from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from flask import jsonify

from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge

from flask_restful import Resource, Api
from flask_restful import reqparse

from flask_cors import CORS

import requests

from .image_converter import ImageConverter

from . import config

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config.from_object(config)

CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

parser = reqparse.RequestParser()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get
