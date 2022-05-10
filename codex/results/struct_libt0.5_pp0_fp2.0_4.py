import _struct
import copy
import os
from PIL import Image
import numpy as np
from scipy.misc import imread
from scipy.misc import imresize
import matplotlib.pyplot as plt
import glob
from PIL import Image

from keras.models import load_model

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

import tensorflow as tf

from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras.layers.normalization import BatchNormalization
from keras.optimizers import SGD,RMSprop,adam
from keras.callbacks import ModelCheckpoint
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Input, Dense, Convolution2D, MaxPooling2D, AveragePooling2
