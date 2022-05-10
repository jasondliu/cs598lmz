import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import os
import time
import random
import numpy as np
import tensorflow as tf
import tensorflow.contrib.slim as slim
from tensorflow.python.ops import control_flow_ops
from tensorflow.python.training import moving_averages

from utils import *
from models import *
from datasets import *
from config import *

# Set random seed
random.seed(SEED)
np.random.seed(SEED)
tf.set_random_seed(SEED)

# Create directories if not exist
if not os.path.isdir(CHECKPOINT_DIR):
    os.makedirs(CHECKPOINT_DIR)
if not os.path.isdir(SAMPLE_DIR):
    os.makedirs(SAMPLE_DIR)

# Placeholders
x_real = tf.placeholder(tf.float32, shape=[None, IMG_HEIGHT, IMG_WIDTH, IMG_CHANNEL], name='x_real')
z_
