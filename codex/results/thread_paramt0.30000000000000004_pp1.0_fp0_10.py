import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import cv2
import numpy as np
import os
import time
import random
import math

from collections import deque

import tensorflow as tf

from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout
from keras.optimizers import Adam
from keras.callbacks import TensorBoard

from skimage.color import rgb2gray
from skimage.transform import resize

from tqdm import tqdm

import matplotlib.pyplot as plt

from PIL import Image

import gym
from gym import wrappers

from scipy.misc import imresize

from keras.models import load_model

from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory

import warnings
warnings.filterwarnings('ignore')

# %
