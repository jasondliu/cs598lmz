import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

#----------------------------------------------------
#-- Import Libraries
#----------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import cv2
import math
import random
import time
import os
import glob

#----------------------------------------------------
#-- Import Modules
#----------------------------------------------------
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Dropout
from keras.layers import Activation
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils
from keras.optimizers import Adam
from keras.models import load_model
from keras.callbacks import ModelCheckpoint
from keras.callbacks import EarlyStopping
from keras.callbacks import ReduceLROnPlateau
from keras.callbacks import TensorBoard

#----------------------------------------------------
#--
