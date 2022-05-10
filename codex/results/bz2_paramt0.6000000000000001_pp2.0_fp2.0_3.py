from bz2 import BZ2Decompressor
BZ2Decompressor

from subprocess import Popen, PIPE, STDOUT

from multiprocessing import Pool
from functools import partial

import os
import time
import sys

import warnings
warnings.filterwarnings('ignore')

from collections import Counter

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

from keras import backend as K
from keras.layers import Dense, BatchNormalization, Dropout
from keras.models import Sequential
from keras.optimizers import Adam
from keras.callbacks import LearningRateScheduler

from tensorflow.python.client import device_lib
from keras.utils import multi_gpu_model

from keras.utils.np_utils import to_categorical

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

from keras.layers import Input, Embedding, LSTM, Lambda, Spatial
