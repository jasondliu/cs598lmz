import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#from __future__ import print_function
import numpy as np
import cv2
import os
from os.path import join, isfile
import sys
from os import listdir
from os.path import isfile, join
import argparse
import random
import time
import shutil
from scipy.misc import imsave
from scipy.misc import imread
from scipy.misc import imresize
import matplotlib.pyplot as plt
from matplotlib import colors
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import csv
import glob

import tensorflow as tf
from keras.models import load_model
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras.optimizers import
