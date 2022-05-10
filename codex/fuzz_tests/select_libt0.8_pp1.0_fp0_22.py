import selectors
import sys
import time

from pytocl import driver
from pytocl.driver import Driver

import numpy as np

from network import Network

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from collections import deque
import random
from util import prepare_data_for_network

class MyDriver(Driver):

    def __init__(self):
        self.network = Network(2, 3)
        self.network.train(10000)
        self.loss_queue = deque(maxlen=100)
        self.reward_queue = deque(maxlen=100)
        self.step = 0
        self.reward = 0

    def load(self, filename):
        with open(filename, "rb") as f:
            while True:
                try:
                    self.network.model.append(pickle.load(f))
                except EOFError:
                    return
    
    def
