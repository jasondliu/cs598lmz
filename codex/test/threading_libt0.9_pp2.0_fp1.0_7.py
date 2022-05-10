import threading
threading.stack_size(2**27)
import sys
import tensorflow as tf
import numpy as np
import cv2
from vgg16 import VGG16
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16

# load model
model = VGG16()

PREP_WIDTH = 700
REQ_WIDTH = 300
IMG_WIDTH = 52
IMG_HEIGHT = 52

# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)


def get_img_wo_bg(frame):
    global PREP_WIDTH

    if frame is None:
        return None

