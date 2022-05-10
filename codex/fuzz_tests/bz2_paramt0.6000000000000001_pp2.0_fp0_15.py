from bz2 import BZ2Decompressor
BZ2Decompressor

import pandas as pd
pd.set_option('display.max_columns', 500)
# pd.set_option('display.max_rows', 500)
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")

from sklearn.preprocessing import LabelBinarizer, LabelEncoder
from sklearn.metrics import confusion_matrix

from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.preprocessing import text, sequence
from keras import utils

from keras.models import Model
from keras.layers import Input, LSTM, Dense

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from sklearn.model_selection import train_test_split

from gensim.models import Word
