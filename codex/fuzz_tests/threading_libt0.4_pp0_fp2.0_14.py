import threading
threading.stack_size(67108864)

import sys
sys.path.append("game/")
import wrapped_flappy_bird as game

import numpy as np
from collections import deque

import tensorflow as tf
import tensorflow.contrib.slim as slim

import gym
import gym_ple

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

class DQN:
    def __init__(self, env, learning_rate=0.001, reward_decay=0.9, e_greedy=0.9, replace_target_iter=300, memory_size=500, batch_size=32, e_greedy_increment=None, output_graph=False):
        self.env = env
        self.n_actions = 2
        self.n_features = 80 * 80
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon_max = e_greedy
        self.replace_target_
