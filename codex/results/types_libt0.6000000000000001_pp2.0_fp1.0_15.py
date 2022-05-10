import types
types.ModuleType.__repr__ = module_repr

import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_log_error

from datetime import datetime
from datetime import timedelta

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

import math

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Activation
from keras.layers import Dropout

from keras import optimizers
from keras import metrics
from keras.callbacks import Callback, EarlyStopping, ModelCheckpoint

import os
import sys

from os.path
