import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

import numpy as np
import pandas as pd
import os
import glob
import sys
import errno

import keras
from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Dropout, Flatten, Input, Conv1D, MaxPooling1D, Conv2D, MaxPooling2D
from keras.layers import LSTM, Bidirectional, TimeDistributed
from keras.layers.normalization import BatchNormalization
from keras import regularizers
from keras.callbacks import ModelCheckpoint

from sklearn.preprocessing import LabelEncoder, StandardScaler, RobustScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

import time
import datetime

# import keras.back
