import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import json
import os
import pandas as pd

from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.layers import Dense, Input, GlobalMaxPooling1D
from keras.layers import Conv1D, MaxPooling1D, Embedding, Flatten
from keras.models import Model
from keras.initializers import Constant
from keras.callbacks import Callback
import keras.backend as K

import pickle

import matplotlib.pyplot as plt
plt.style.use('ggplot')
%matplotlib inline

import numpy as np

# Set random seed
np.random.seed(42)

# Get data
base_path = os.getc
