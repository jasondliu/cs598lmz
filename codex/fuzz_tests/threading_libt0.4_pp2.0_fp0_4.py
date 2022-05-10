import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
import time
import random
import numpy as np
from copy import deepcopy
from numpy import array
from numpy import argmax
from numpy import array_equal
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import TimeDistributed
from keras.layers import RepeatVector
from keras.utils import plot_model
from keras.callbacks import ModelCheckpoint
from keras.callbacks import EarlyStopping
from keras.models import load_model

def get_model(n_input, n_output, n_units):
    model = Sequential()
    model.add(LSTM(n_units, activation='relu', input_shape=(n_input, 1)))
    model.add(RepeatVector(n_output))
    model.add(LSTM(n_units, activation='relu', return_sequences=True))
    model.
