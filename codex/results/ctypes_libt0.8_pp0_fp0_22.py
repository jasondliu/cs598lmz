import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(os.path.dirname(BASE_DIR))
import modelnet_dataset
import gc

import tensorflow as tf
import numpy as np


BATCH_SIZE = 1
NUM_POINT = 2048
NUM_CHANNEL = 3
NUM_CLASSES = 40

print('Preparing model...')

sess = tf.Session()

# placeholders
inputs = tf.placeholder(tf.float32, shape=(BATCH_SIZE,NUM_POINT,NUM_CHANNEL))
labels = tf.placeholder(tf.int32, shape=(BATCH_SIZE,))
labels_one_hot = tf.one_hot(labels, NUM_CLASSES)
is_training = tf.placeholder(tf.bool, shape=())

# load model
with tf.device('
