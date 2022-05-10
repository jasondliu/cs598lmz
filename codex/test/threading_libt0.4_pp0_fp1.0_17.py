import threading
threading.stack_size(2**27)
import sys
import os

from scipy.misc import imread, imresize
import numpy as np
import tensorflow as tf
from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, Dropout, Flatten, Lambda, ELU, MaxPooling2D, Cropping2D
from keras.layers.convolutional import Convolution2D
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.regularizers import l2
from keras import backend as K
from keras.utils import np_utils
from keras.preprocessing.image import ImageDataGenerator
from keras.models import model_from_json
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import csv
import cv2

# import data from csv file
samples = []
