import ctypes
ctypes.cast(0, ctypes.py_object).value = None

import matplotlib.pyplot as plt
import numpy as np
import os
import re
import sys
import time
import tensorflow as tf
import tensorflow.contrib.slim as slim
import tensorflow.contrib.slim.nets as nets
from PIL import Image

def get_one_image(img_dir):
    image = Image.open(img_dir)
    plt.imshow(image)
    image = image.resize([224, 224])
    image = np.array(image)
    return image

def evaluate_one_image(image_array):
    with tf.Graph().as_default():
        BATCH_SIZE = 1
        N_CLASSES = 2

        image = tf.cast(image_array, tf.float32)
        image = tf.reshape(image, [1, 224, 224, 3])
        image = tf.cast(image, tf.float32)
        image = tf.image.per_image_standardization(image)

