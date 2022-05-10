import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

import tensorflow as tf
tf.compat.v1.disable_eager_execution()

from keras import backend as K
from keras.models import load_model
import numpy as np
import cv2
import time
import glob


model = load_model('../models/model.h5')

def resize_image(image):
    height, width = image.shape[:2]
    if height > width:
        new_height = 600
        new_width = int(image.shape[1] * new_height / image.shape[0])
    else:
        new_width = 600
        new_height = int(image.shape[0] * new_width / image.shape[1])
    image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
    return image

