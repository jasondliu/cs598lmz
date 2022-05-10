import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
from PIL import ImageGrab
import numpy as np
from PIL import Image
from os import system
from PIL import ImageOps
import time
from numpy import *
from directkeys import ReleaseKey, PressKey, W, A, S, D
from grabscreen import grab_screen
from getkeys import key_check
import cv2
from collections import deque
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Activation, Flatten
from keras.optimizers import Adam
from keras.callbacks import TensorBoard
import matplotlib.pyplot as plt
import random
import time

##
WIDTH = 120
HEIGHT = 60
LR = 1e-3
EPOCHS = 10

t_time = 0.25

###
##
model = Sequential()
model.add(Conv2D(256, (3, 3), input_shape=(WIDTH, HEIGHT, 3)))

