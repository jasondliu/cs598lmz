import threading
threading.stack_size(1024*1024*1024)

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from utils import *
from config import *

import numpy as np
import pandas as pd

import pickle
from datetime import datetime

from sklearn import preprocessing
from sklearn.metrics import log_loss

from keras.models import Sequential, Model
from keras.layers import Dense, Dropout, Activation, Flatten, Input, merge, Embedding, LSTM, Bidirectional, GlobalAveragePooling1D, GlobalMaxPooling1D, Convolution1D, MaxPooling1D
from keras.layers.merge import Concatenate
from keras.layers.normalization import BatchNormalization
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.layers.advanced_activations import PReLU
from keras.preprocessing import sequence
from keras import backend as K
