import lzma
lzma.LZMAError

import json

import numpy as np

import pandas as pd

import tensorflow as tf
import tensorflow_hub as hub

import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from keras.utils.np_utils import to_categorical

from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint

from keras.models import load_model

from sklearn.model_selection import train_test_split

from sklearn.metrics import confusion_matrix

import re

import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

import matplotlib.pyplot as plt

import seaborn as sns

import warnings
warnings.filterwarnings('ignore')
