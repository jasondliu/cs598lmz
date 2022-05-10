import lzma
lzma.LZMAError

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import Adam
from keras.utils import to_categorical

import tensorflow as tf

from keras.layers import Input, Flatten, Conv2D, MaxPooling2D, Dense, Dropout, BatchNormalization, Activation
from keras.models import Model

from keras.callbacks import ModelCheckpoint

import keras.backend as K

from keras.preprocessing.image import ImageDataGenerator

from keras.models import load_model

from keras.utils import plot_model

from keras.regularizers import l2

from sklearn.metrics import confusion_matrix

from keras.callbacks import ReduceLROnPlate
