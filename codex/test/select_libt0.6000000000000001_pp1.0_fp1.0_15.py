import select
from collections import deque
from datetime import datetime
from io import BytesIO
from PIL import Image

import numpy as np
import cv2
from flask import Flask, render_template, Response, request, send_file
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.mobilenet import preprocess_input
from keras.applications.mobilenet import decode_predictions

from picamera import PiCamera
from picamera.array import PiRGBArray

# Pre-process image
def preprocess(img):
    img = cv2.resize(img, (224, 224))
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img

# Classify image
def classify(img):
    # Load model
    model = load_model('model/model.h5')

    # Make prediction
    preds = model.predict(img)
    return preds

# Create flask app
