import sys, threading
threading.Thread(target=lambda: sys.stdout.write('')).start()

sys.path.insert(0, "./")
sys.path.insert(0, "./research/")
sys.path.insert(0, "./research/feature_extraction/")

import numpy as np

import tensorflow as tf
import tensorflow.keras as keras

import tensorflow.keras.backend as K

import numpy as np
import ssl
import sklearn

# for VGG
import cv2

# for plots
import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# for feature extraction
import librosa

# for the feature database
import sqlite3, pickle

# for data augmentation
import imgaug as ia
import imgaug.augmenters as iaa

# for database management
import database.db_management as db
import database.db_sqlite as dbsql

import feature_extraction.feature_extraction_scripts as feat
import feature_
