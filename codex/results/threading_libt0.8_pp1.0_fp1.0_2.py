import threading
threading.stack_size(2**27)
import gc
import re
from collections import defaultdict
import datetime
import pickle
import os
from sklearn import metrics

from keras.preprocessing.sequence import pad_sequences
from keras.layers import Input, Dropout, Dense, BatchNormalization, Activation, concatenate, GRU, Embedding, Flatten, BatchNormalization
from keras.models import Model
from keras.callbacks import ModelCheckpoint, Callback, EarlyStopping
from keras import backend as K
from keras import optimizers
from keras import initializers
from keras.utils import plot_model
import keras_metrics

def rmse(y_true, y_pred):
    return K.sqrt(K.mean(K.square(y_pred - y_true)))

# https://www.kaggle.com/sudalairajkumar/simple-exploration-baseline-notebook-avito/comments
# https://www.kaggle.com/ogrellier/no-leak
