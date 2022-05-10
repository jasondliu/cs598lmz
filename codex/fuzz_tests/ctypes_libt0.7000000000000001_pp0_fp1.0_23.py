import ctypes
ctypes.windll.user32.SetProcessDPIAware()
import matplotlib.pyplot as plt
import numpy as np
import os
import io
import base64
import sys
from IPython.display import HTML
import time
import tensorflow as tf
import tensorflow.keras as keras

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import Adam

from PIL import Image

%matplotlib inline
plt.rcParams['figure.figsize'] = [9, 6]



def get_mnist_dataset():
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    x_train = x_train.reshape(60000, 784)
    x_test = x_test.reshape(10000, 784)
    x_train = x_train.astype('float32')
    x_test =
