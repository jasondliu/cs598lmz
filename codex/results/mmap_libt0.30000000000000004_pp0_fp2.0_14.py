import mmap
import numpy as np
import os
import pickle
import random
import re
import sys
import tensorflow as tf
import time

from collections import defaultdict

from keras.models import Sequential, Model
from keras.layers import Dense, Dropout, Input, Lambda, LSTM, Masking, TimeDistributed, Bidirectional
from keras.layers.merge import Concatenate, Dot, Multiply
from keras.layers.embeddings import Embedding
from keras.layers.normalization import BatchNormalization
from keras.layers.advanced_activations import PReLU
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.utils import to_categorical
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.optimizers import Adadelta
from keras.initializers import RandomUniform
from keras import backend as K

from sklearn.model_selection import train_test_split
from sklearn.
