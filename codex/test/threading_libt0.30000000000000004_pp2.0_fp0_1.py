import threading
threading.stack_size(67108864)

import sys
import time
import numpy as np
import cv2
import os
import glob
import json
import base64
import requests

from picamera.array import PiRGBArray
from picamera import PiCamera

from time import sleep

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask_restful import Api
from flask_restful import Resource

from flask_socketio import SocketIO

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from flask_heroku import Heroku

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

from flask_bcrypt import Bcrypt

from flask_mail import Mail, Message

from flask_cors import CORS

from flask_socketio import SocketIO, emit

from flask_wtf import FlaskForm
