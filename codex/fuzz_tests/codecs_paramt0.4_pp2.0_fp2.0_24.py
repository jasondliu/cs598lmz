import codecs
codecs.register_error('strict', codecs.ignore_errors)

import numpy as np
import matplotlib.pyplot as plt

# from scipy.io import wavfile
# from scipy.io.wavfile import write

from scipy.signal import butter, lfilter

# from scipy.signal import spectrogram

import wave

import os

import pickle

import random

import copy

import math

import sys

# import tensorflow as tf

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

import keras

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Flatten, Conv2D, MaxPooling2D, LSTM, TimeDistributed
from keras.layers.normalization import BatchNormalization
from keras.callbacks import ModelCheckpoint
from keras.models import model_from_json

from keras import backend as K

from keras.utils import np_utils


