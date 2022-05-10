import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

import numpy as np
import pandas as pd
import argparse
import pickle as pkl

from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import average_precision_score

from keras.models import Model
from keras.layers import Input, Dense, Dropout, Activation
from keras.optimizers import SGD, Adam
from keras.regularizers import l1, l2
from keras.utils import np_utils
from keras import initializers
from keras.callbacks import EarlyStopping, ReduceLROnPlateau
from keras.models import load_model


def get_seq_length(max_l, pssm_size=20):
    with open('features/train_set.fa', 'r') as f:
        seq_len = 0
