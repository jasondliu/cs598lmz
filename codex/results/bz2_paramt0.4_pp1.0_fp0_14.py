from bz2 import BZ2Decompressor
BZ2Decompressor

from gzip import GzipFile
GzipFile

from zlib import decompress
decompress

import sys
sys.path.append('..')
from dl_progress import dl_progress
dl_progress

import numpy as np
np

import matplotlib.pyplot as plt
plt

import tensorflow as tf
tf

from tensorflow.examples.tutorials.mnist import input_data
input_data

mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)
mnist

sess = tf.InteractiveSession()
sess

x = tf.placeholder(tf.float32, shape=[None, 784])
x

y_ = tf.placeholder(tf.float32, shape=[None, 10])
y_

W = tf.Variable(tf.zeros([784,10]))
W

b = tf.Variable(tf.zeros([10]))
b

sess.run(tf.global_variables_initializer
