import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H'),daemon=True).start()

from IPython.display import clear_output

import matplotlib.pyplot as plt

import gym
from gym import spaces
from gym.utils import seeding

import numpy as np

from collections import deque

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras import backend as K

EPISODES = 1000

class CartPoleEnv:
    def __init__(self):
        self.env = gym.make('CartPole-v1')
        self.env.reset()
        self.action_space = self.env.action_space.n
        self.observation_space = self.env.observation_space.shape[0]
        self.episode_count = 0
        self.step_count = 0
        self.done = False
        self.score = 0

    def reset(self):
        self.env
