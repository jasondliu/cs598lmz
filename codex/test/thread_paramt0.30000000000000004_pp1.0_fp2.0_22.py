import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import time

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM, CuDNNLSTM, BatchNormalization
from tensorflow.keras.callbacks import TensorBoard, ModelCheckpoint

from sklearn.preprocessing import MinMaxScaler

from collections import deque

from datetime import datetime

from tqdm import tqdm

#%%

def get_data(filename, seq_len, normalise_window):
    data = pd.read_csv(filename, index_col=0)
    data = data.drop(columns=['Open', 'High', 'Low', 'Adj Close', 'Volume'])
    data = data.rename(columns={'Close': 'Price'})
    data
