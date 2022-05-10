import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import numpy as np
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
import keras
import keras.backend as K
from keras import layers
from keras.models import Model, Sequential
from keras.optimizers import Adam
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import os

os.environ["CUDA_VISIBLE_DEVICES"]="0"

#%%

def load_data(data_path):
    """
    Load data from data path.
    """
    # Load meta data from text files.
    with open(data_path + 'meta.txt', 'r') as f:
        meta_data = f.read().splitlines()
    image_paths = []
    labels = []
    for meta in meta_data:
        image_paths.append(meta.split(' ')[0])
        labels.append(int(meta.split(' ')[1]))

