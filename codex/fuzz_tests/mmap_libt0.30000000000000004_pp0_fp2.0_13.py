import mmap
import numpy as np
import os
import sys
import time

from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import class_weight

from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
from keras.models import Sequential
from keras.utils import to_categorical

from PIL import Image

def get_data(path):
    """
    Loads the data from the specified path.
    """
    X = []
    y = []
    for folder in os.listdir(path):
        for file in os.listdir(path + folder):
            img = Image.open(path + folder + '/' + file)
            img = img.resize((200, 200))
            X.append(np.array(img))
            y.append(folder)
    return np.array(X), np
