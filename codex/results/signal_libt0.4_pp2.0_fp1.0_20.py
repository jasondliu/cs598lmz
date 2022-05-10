import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time
import random
import numpy as np
import tensorflow as tf
from collections import deque
from keras.models import Model, Sequential
from keras.layers import Dense, Input, Flatten, Conv2D, MaxPooling2D, Activation, BatchNormalization
from keras.optimizers import RMSprop
from keras import backend as K
from keras.utils import plot_model
from keras.models import load_model

from vizdoom import *

# Q-learning hyperparameters
learning_rate = 0.00025
# learning_rate = 0.0001
discount_factor = 0.99
epochs = 20
learning_steps_per_epoch = 2000
replay_memory_size = 10000

# NN learning hyperparameters
batch_size = 64

# Training regime
test_episodes_per_epoch = 100

# Image params
resolution = (30, 45)

# Other parameters

