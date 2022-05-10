import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H'),daemon=True).start()

# if you want to run with GPU, please make sure you have the right to use it
# and also make sure you have enough memory to support the training,
# otherwise you might get cuda runtime error(out of memory).
# os.environ['CUDA_VISIBLE_DEVICES'] = '1'

import numpy as np
import gym
from gym import error, spaces, utils
from gym.utils import seeding
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random
import math
import logging
import time
import sys

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.backend import clear_session
from collections import deque
from collections import OrderedDict

#import arc
#import environment

#from keras.layers import Input, Reshape, Dropout
