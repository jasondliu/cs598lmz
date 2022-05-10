import threading
threading.stack_size(2**27)
import sys
import glob
sys.path.append('../../')
sys.path.append('../')
sys.path.append('./')
from keras.models import Sequential, Model, model_from_json
from keras.layers.core import Dense, Dropout, Activation, Flatten, Reshape, Permute, Lambda
from keras.layers import Input, merge, ELU
from keras.layers.convolutional import Conv2D, MaxPooling2D, ZeroPadding2D, UpSampling2D, AveragePooling2D, Conv2DTranspose
from keras.layers.normalization import BatchNormalization
from keras.regularizers import l2
import keras.backend as K
import json
from keras.utils import np_utils
# import theano
import keras.optimizers as optimizers
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(2016)

