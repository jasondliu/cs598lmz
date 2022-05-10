import ctypes
ctypes.cdll.LoadLibrary('libcudart.so')
ctypes.cdll.LoadLibrary('libcublas.so')
ctypes.cdll.LoadLibrary('libcufft.so')
ctypes.cdll.LoadLibrary('libcurand.so')
ctypes.cdll.LoadLibrary('libcusparse.so')
ctypes.cdll.LoadLibrary('libcusolver.so')

import numpy as np
import tensorflow as tf
import time

# Create a graph
g = tf.Graph()
with g.as_default():
    with tf.device("/gpu:0"):
        # Define operations and tensors in `graph`.
        a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
        c = tf.matmul(a, b)

# Creates a session with log
