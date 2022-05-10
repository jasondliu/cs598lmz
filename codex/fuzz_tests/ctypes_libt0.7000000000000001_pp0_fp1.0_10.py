import ctypes
ctypes.CDLL('libc.so.6').srand(64)

# Make deterministic
random.seed(64)
np.random.seed(64)

# import necessary libraries
import os
import glob
import shutil
import cv2
import math
import tqdm
import joblib
import random
import datetime
import argparse
import pandas as pd
import numpy as np
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import backend as K
from tensorflow.keras.layers import Input, Conv2D, Activation, BatchNormalization, LeakyReLU, Add, Lambda, MaxPooling2D, UpSampling2D, Concatenate, ZeroPadding2D, AveragePooling2D, DepthwiseConv2D
from tensorflow.keras.models import Model
from tensorflow.keras.utils import Sequence
from tensorflow.keras.activations import sigmoid
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.call
