import mmap
import struct
import six
import numpy as np
from numpy import zeros
from numpy import array

from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.optimizers import SGD
from keras.optimizers import RMSprop, Adagrad
from keras.optimizers import Adam, Adadelta

from sklearn.metrics import confusion_matrix
