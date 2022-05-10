import threading
threading.stack_size(1024*1024)

import os
import sys
import time
import json
import math
import random
import numpy as np
import pandas as pd

import keras
import tensorflow as tf

from keras import backend as K
from keras.models import Model, Sequential
from keras.layers import Input, Dense, Conv2D, Flatten, MaxPooling2D, Dropout, Reshape
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Usage: python3.5 cnn.py <train|test> <game> <player> <model_file>

# cfg.py contains dictionary of game configurations
import cfg

game = sys.argv[2]
player = int(sys.argv[3])
model_file = sys.argv[4]

