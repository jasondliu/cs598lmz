import socketio
from socketio import Namespace
import eventlet
import eventlet.wsgi
import time
from flask import Flask, render_template
from keras.models import load_model
from keras.preprocessing.image import array_to_img, img_to_array
import tensorflow as tf
import numpy as np
from PIL import Image
import cv2
from io import BytesIO
import base64
from alpr_util import *
from variables import *

def gen():
    model = load_model(MODEL_FILENAME)
    graph = tf.get_default_graph()
    offset = 0
    vehicle_plate = 0
    print("loaded model!")
    while True:
        img = yield (
            'data:image/jpeg;base64,' + base64.b64encode(bytes(imgBytes)).decode('ascii'))


        imgBytes = img.read()
        # convert bytes data to PIL Image obj
        imgPIL = Image.open(io.BytesIO(imgBytes))
        # convert PIL Image obj
