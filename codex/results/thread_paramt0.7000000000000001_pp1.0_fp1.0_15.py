import sys, threading
threading.Thread(target=lambda: sys.stdin.read()).start()

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

from get_data import get_data, get_data_old
from model import create_model

import cv2
import time
import numpy as np
import tensorflow as tf
import keras

from keras.models import Model
from keras.utils import plot_model
from keras.applications import imagenet_utils
from keras.preprocessing.image import img_to_array
from keras.optimizers import SGD
from keras.layers import Dense, Dropout, Activation, Flatten, Input
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization
from keras.layers import Concatenate
from keras.callbacks import EarlyStopping, ModelCheckpoint

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from imutils import paths

from sklearn.model_selection import train
