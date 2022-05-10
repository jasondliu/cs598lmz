import types
types.FunctionType = types.LambdaType

# import the necessary packages
from collections import OrderedDict
import numpy as np
import cv2
import time

# import the necessary packages
from tensorflow.keras.models import load_model
import os

# load the pre-trained model
print("[INFO] loading pre-trained network...")
model = load_model(args["model"])

# initialize the class labels dictionary
CLASSES = OrderedDict({
    0: 'background',
    1: 'person',
    2: 'bicycle',
    3: 'car',
    4: 'motorcycle',
    5: 'airplane',
    6: 'bus',
    7: 'train',
    8: 'truck',
    9: 'boat',
    10: 'traffic light',
    11: 'fire hydrant',
    12: 'stop sign',
    13: 'parking meter',
    14: 'bench',
    15: 'bird',
    16: 'cat',
    17: 'dog',
    18:
