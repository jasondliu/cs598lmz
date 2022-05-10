import threading
threading.stack_size(64000000)

import os
import sys
import cv2
import matplotlib.pyplot as plt
import numpy as np
import face_recognition
from PIL import Image
import math
import time
import datetime
import scipy.stats
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Normalizer
from sklearn.svm import SVC
import pickle
import mtcnn
from mtcnn import MTCNN
import tensorflow as tf
from tensorflow.keras import layers, models
from keras.layers import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pickle

print(tf.__version__)

config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth
