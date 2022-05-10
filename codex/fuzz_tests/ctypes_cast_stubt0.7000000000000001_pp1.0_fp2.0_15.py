import ctypes
ctypes.cast(0x08000000, ctypes.py_object).value = 0x20000000
sys.getrecursionlimit()

sys.setcheckinterval(100)

#sys.path.append('/home/student/anaconda3/envs/tensorflow_cpu/lib/python3.6/site-packages')
sys.path.append('/home/student/anaconda3/lib/python3.6/site-packages')

import tensorflow as tf
import numpy as np
from keras import backend as K

import pandas as pd
import numpy as np
np.random.seed(123)  # for reproducibility
 
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras.datasets import mnist
import matplotlib.pyplot as plt
%matplotlib inline

from keras.datasets import mnist
