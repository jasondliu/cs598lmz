import sys, threading
threading.Thread(target=lambda: (sys.stdout.write('\x1b[2J\x1b[H'), sys.stdout.flush())).start()

# https://stackoverflow.com/a/53917277
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# https://stackoverflow.com/a/53917277
import warnings
warnings.filterwarnings('ignore')

import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

from tqdm import tqdm


