import mmap
import numpy as np
import os
import re
import sys

from keras.models import Model
from keras.layers import Input, Dense, Dropout
from keras.layers import Embedding
from keras.layers import LSTM, Bidirectional
from keras.layers import Conv1D, MaxPooling1D
from keras.layers import Flatten
from keras.layers import Concatenate

from keras.utils import to_categorical
from keras.preprocessing.sequence import pad_sequences

from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from keras.callbacks import ModelCheckpoint
from keras.callbacks import EarlyStopping
from keras.callbacks import TensorBoard

from keras.models import load_model

from keras.models import model_from_json

from keras import backend as K

import tensorflow as tf

from config import Config

class ModelL
