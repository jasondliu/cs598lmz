from lzma import LZMADecompressor
LZMADecompressor

import numpy as np
import pandas as pd
import tensorflow as tf
import os
import sys
import time

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers.normalization import BatchNormalization
from keras.layers import Conv2D, MaxPooling2D, Flatten
from keras.callbacks import EarlyStopping, ModelCheckpoint

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc, accuracy_score, confusion_matrix, classification_report

from sklearn.metrics import confusion_matrix

import matplotlib
import matplotlib.pyplot as plt

from IPython.display import clear_output

import random

#DATASET_URL = 'https://github.com/zalandoresearch/fashion-mnist/raw/master/data/fashion/'
#FILENAME = 't10k-images-idx3-ubyte'
#file
