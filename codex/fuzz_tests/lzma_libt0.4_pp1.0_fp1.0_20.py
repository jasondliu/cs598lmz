import lzma
lzma.open
import sys
sys.path.append("/home/pi/Desktop/ssd_keras")
from ssd import SSD300
from ssd_utils import BBoxUtility
import numpy as np
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import TensorBoard
import os
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

%matplotlib inline

# Set the input image size.
img_height = 300
img_width = 300

# 1: Build the Keras model.

K.clear_session() # Clear previous models from memory.

model = SSD300(image_size=(img_height, img_width, 3),
                n_classes=20,
                mode='training',
                l2_regularization
