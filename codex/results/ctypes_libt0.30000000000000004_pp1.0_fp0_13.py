import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import numpy as np
import cv2
import os
import sys
import time
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels

from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

from PIL import Image

import itertools

from keras.utils import plot_model

from keras import backend as K

import matplotlib.pyplot as plt

from sklearn.metrics import roc
