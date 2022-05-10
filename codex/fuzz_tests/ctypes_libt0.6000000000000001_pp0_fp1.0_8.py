import ctypes
ctypes.windll.user32.SetProcessDPIAware()

from PIL import Image
import numpy as np
import pickle
import time

import tensorflow as tf
import keras
from keras.applications.resnet50 import ResNet50
from keras.optimizers import SGD
from keras import backend as K

from keras.preprocessing.image import ImageDataGenerator

from keras.models import Model
from keras.layers import Dense, Dropout, Activation, Flatten, Input
from keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D, GlobalMaxPooling2D, AveragePooling2D
from keras.layers.normalization import BatchNormalization
from keras.regularizers import l2

from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
%matplotlib inline

import skimage
from skimage.transform import resize

import os
import glob

import pandas
