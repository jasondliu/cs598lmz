import codecs
codecs.register_error('ignore', codecs.replace_errors)

# TensorFlow
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models

# Numpy
import numpy as np

# Sklearn
from sklearn import preprocessing

# Matplotlib
import matplotlib.pyplot as plt

# Misc
import json
import pickle
import collections
import random
import time

# Local imports
from utils import *
from model import *
from dataset import *

# Set random seeds
random.seed(123)
np.random.seed(123)
tf.random.set_seed(123)

# Global config
batch_size = 16
epochs = 10

# Load dataset
with codecs.open('data/dataset.json', 'r', 'utf-8') as f:
    dataset = json.load(f)

# Create vocabulary
vocab_size = 5000
tokenizer = keras.preprocessing.text.Tokenizer(num_words=vocab_size, oov_token="
