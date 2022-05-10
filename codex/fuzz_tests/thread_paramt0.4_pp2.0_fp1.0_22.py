import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import os
import time
import shutil
import numpy as np
import pandas as pd
import tensorflow as tf

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras.optimizers import SGD, Adam
from tensorflow.keras.utils import to_categorical

from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model

from PIL import Image

from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model

from PIL import Image

