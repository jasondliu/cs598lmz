import sys, threading
threading.Thread(target=lambda:sys.stdin.read(1)).start()

import parameters
import copy
import cv2
import numpy as np
from keras.models import model_from_json
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.optimizers import SGD , Adam
from keras.utils import np_utils
from keras.models import load_model
import tensorflow as tf
import random
from collections import deque
import time


class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=parameters.MEMORY_SIZE)
        self.gamma = 0.95    # discount rate
        self.epsilon = parameters.INITIAL_EPSILON
        self.epsilon_min = parameters.MIN_EPSIL
