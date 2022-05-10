import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import os
import time
import numpy as np
import tensorflow as tf
import tensorflow.contrib.slim as slim
import scipy.misc
import scipy.io
import matplotlib.pyplot as plt

from PIL import Image

from utils import *
from network import *
from dataloader import *

import cv2

# Parameters
learning_rate = 0.0001
batch_size = 1

# Network Parameters
image_size = 256
label_size = 256
c_dim = 3

# Train Directories
checkpoint_dir = './checkpoint'
sample_dir = './sample'

# Test Directories
test_dir = './test'

# Function to load the checkpoint
def load(saver, sess, checkpoint_dir):
    import re
    print(" [*] Reading checkpoints...")
    ckpt = tf.train.get_checkpoint_state(checkpoint_dir)
