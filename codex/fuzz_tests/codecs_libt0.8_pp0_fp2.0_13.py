import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
tf.__version__

from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
"""from pandas_datareader import data

from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.callbacks import EarlyStopping
from keras.optimizers import Adam
from keras import backend as K
from keras.callbacks import TensorBoard
from time import time

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import
