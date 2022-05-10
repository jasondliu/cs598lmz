import threading
threading.stack_size(2**27)

# Disable tensorflow compilation warnings
# os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

from datetime import datetime
# from scipy.misc import imread
import json
import numpy as np
from scipy.misc import imresize
from scipy.misc import imsave
from sklearn.preprocessing import OneHotEncoder
from scipy.io import loadmat
from skimage import img_as_float
from skimage.filters import threshold_otsu
from skimage.morphology import closing, square

from urllib.request import urlopen,urlretrieve

from skimage.io import imread
from skimage import color
from scipy.ndimage import zoom

from random import random
import os
from scipy.misc import imread

from tqdm import tqdm
from time import time

from keras.layers import Input, Dense, Convolution2D, MaxPooling2D, AveragePooling2
