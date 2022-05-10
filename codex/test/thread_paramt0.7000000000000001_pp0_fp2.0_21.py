import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

from IPython.display import clear_output
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
import os
from collections import deque
import random
from keras import backend as K
import numpy as np
import matplotlib.pyplot as plt
from gym import wrappers

import tensorflow as tf

class DQNAgent():
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=2000)
        self.gamma = 0.95    # discount rate
        self.epsilon = 1.0  # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.001
        self.model = self._build_model()
