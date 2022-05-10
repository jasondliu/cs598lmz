import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import random
import time
import os

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, Conv2D, MaxPooling2D
from keras.optimizers import Adam

from rl.agents.dqn import DQNAgent
from rl.policy import EpsGreedyQPolicy
from rl.memory import SequentialMemory

from keras.models import load_model

from keras.backend.tensorflow_backend import set_session
import tensorflow as tf

from keras.utils import plot_model

from keras import backend as K

import gym

from gym import wrappers

import cv2

from keras.utils.vis_utils import model_to_dot



