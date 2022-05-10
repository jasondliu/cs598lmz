import signal
signal.alarm(3)

import os, urllib
import tarfile
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import scipy.io
from six.moves import urllib
import tensorflow as tf
from collections import namedtuple
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing
from sklearn.model_selection import StratifiedKFold

# code from https://github.com/hwalsuklee/tensorflow-MNIST-STL-tutorial/


FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string("train_dir", "save_train_dir", "where to save the training file")
tf.app.flags.DEFINE_string("data_dir", "save_data_dir", "where to save the data")
NUM_CLASSES = 10

#Download the dataset
DATA_URL = 'http://ufldl.stanford.edu/housenumbers/'
"""
def maybe_download(
