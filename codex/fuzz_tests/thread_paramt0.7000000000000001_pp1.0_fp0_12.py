import sys, threading
threading.Thread(target=lambda:sys.stdout.write('\n'*100)).start()

import numpy
import time
import pandas
import os
import sys
import logging
import argparse
import pickle
import gc

from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.model_selection import StratifiedKFold, KFold

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from joblib import Parallel, delayed

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import tensorflow as tf

from keras.models import Model, Sequential
from keras.layers import Dense, Activation, BatchNormalization, Dropout, Input
from keras.layers import Embedding, Flatten
from keras.layers import concatenate
from keras.optimizers import Adam
from keras import backend as K

from keras.callbacks import EarlyStopping

from keras.utils import plot_
