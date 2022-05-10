import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H'),daemon=True).start()

import numpy as np
from numpy import random
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.layers import Dense, Input, Reshape, Flatten, Conv2D, MaxPooling2D
import gym
import gym.spaces
import mujoco_py
import time

class DQN(keras.Model):
    def __init__(self, state_dim, action_n, hidden_dim=256):
        super().__init__()
        self.input = Input(shape=(state_dim,))
        self.fc1 = Dense(hidden_dim, activation='relu')
        self.fc2 = Dense(hidden_dim, activation='relu')
        self.fc3 = Dense(action_n, activation='linear', kernel_initializer='zeros')
    
    def __call__(self, inputs):
        x = self.input(input
