import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

#----------------------------
#
#----------------------------
import matplotlib.pyplot as plt
import numpy as np
import os
import time
import tensorflow as tf
import cv2

from config import *
from tensorflow.python.framework import ops
from tensorflow.python.framework import dtypes
import tensorflow.contrib.slim as slim

#----------------------------
#
#----------------------------
def get_files(file_dir):
    '''
    Args:
        file_dir: file directory
    Returns:
        list of images and labels
    '''
    cats = []
    label_cats = []
    dogs = []
    label_dogs = []
    for file in os.listdir(file_dir):
        name = file.split(sep='.')
        if name[0]=='cat':
            cats.append(file_dir + file)
            label_cats.append(0)
        else
