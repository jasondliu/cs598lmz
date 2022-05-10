import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util
from pymunk import Vec2d
import math
import random
import copy
import os
import time
import numpy as np
import pickle
from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras import backend as K

# Hyper Parameters:
GAMMA = 0.95 # discount factor
LEARNING_RATE = 0.001

MEMORY_SIZE = 1000000
BATCH_SIZE = 20

EXPLORATION_MAX = 1.0
EXPLORATION_MIN = 0.01
EXPLORATION_DECAY = 0.995


# Create models folder:
if not os.path.exists('models'):
    os.makedirs('models')

