import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

import tensorflow as tf
from keras.layers import Input, Dense, Concatenate
from keras.models import Model
from keras import optimizers
from keras import backend as K
import keras

import numpy as np

from sklearn.utils import shuffle
from sklearn import preprocessing
from sklearn.metrics import roc_auc_score, roc_curve
import matplotlib.pylab as plt
import argparse
import math
import time
import copy

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--epoch', type=int, default=100)
    parser.add_argument('--data_dir', type=str, default='data')
    parser.add
