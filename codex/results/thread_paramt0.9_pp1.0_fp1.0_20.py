import sys, threading
threading.Thread(target=lambda: sys.stdout.write('stop\n')).start()

import warnings
warnings.filterwarnings(action='ignore')

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
import numpy as np
import math
import matplotlib.pyplot as plt
from pandas import read_csv
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, LSTM
from keras.callbacks import EarlyStopping, ModelCheckpoint


def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset) - look_back):
        a = dataset[i:(i + look_back), 0]
        dataX.append(a)
        dataY.append(dataset[
