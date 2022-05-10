import ctypes
ctypes.cdll.LoadLibrary('libohsu.so')

import sys
sys.path.append('/home/sj/code/TensorFlow/TensorFlow_Tutorial/cnn_mnist')
import tensorflow as tf
import os
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import cifar10_input
import cifar10

img_rows = 32
img_cols = 32
img_channels = 3

num_classes = 10
CKPT_PATH = '/home/sj/code/TensorFlow/TensorFlow_Tutorial/cnn_mnist/model/'

def load_graph(frozen_graph_filename):
    with tf.gfile.GFile(frozen_graph_filename, "rb") as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())

    with tf.Graph().as_default() as graph:
        tf.import_graph_def(
            graph
