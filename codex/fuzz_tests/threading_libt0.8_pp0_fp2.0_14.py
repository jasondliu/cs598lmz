import threading
threading.stack_size(2**27)
import sys
import matplotlib.pyplot as plt
sys.path.append('../../datasets/MNIST_data')
from util import *
from load import mnist
import numpy as np
import time

# step 1: load data, transform it to standard format
print("step 1: load data...")
img_size = 28
train_set = mnist(batch_size=100) # sample size is 100
test_set = mnist(batch_size=100, is_training=False)

# step 2: define parameters and model
print("step 2: define parameters and model...")
n_label = train_set.n_label
print(n_label)
img_h = img_size
img_w = img_size
img_size_flat = img_h * img_w
x = tf.placeholder(tf.float32, shape=[None, img_size_flat], name='x')
x_image = tf.reshape(x, [-1, img_w, img_h, 1
