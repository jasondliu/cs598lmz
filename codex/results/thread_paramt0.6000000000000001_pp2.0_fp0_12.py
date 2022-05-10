import sys, threading
threading.Thread(target=lambda: sys.stdout.write("")).start()
import time
time.sleep(2)

import os
import tensorflow as tf
from keras.backend.tensorflow_backend import set_session

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
set_session(tf.Session(config=config))

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

from sklearn.model_selection import train_test_split

def main():
    filename = "../data_preprocess/data_shakespeare.txt"
    raw_text = open(filename, 'r', encoding='utf-8').read()
    raw_text = raw_text.lower()

    chars = sorted(list(set(raw_text)))
    char_
