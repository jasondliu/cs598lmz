import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)
import os
import sys
import re
import numpy as np

from sklearn.utils import shuffle
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import GradientBoostingClassifier
import xgboost as xgb

from keras.models import Sequential, Model
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM, GRU
from keras.layers.convolutional import Convolution1D, MaxPooling1D
from keras.callbacks import ModelCheckpoint
from keras.layers.normalization import BatchNormalization
from keras.utils import np_utils


def shuffle_weights(model, weights=None):
	if weights is not None:
		assert len(model.layers) == len(weights)
	
