import threading
threading.stack_size(2**27)
import sys
import pickle
sys.setrecursionlimit(10**7)

from sklearn.model_selection import train_test_split

from keras.models import Sequential
from keras.layers import Dense, Activation, Input, Dropout
from keras.layers import CuDNNGRU
from keras.layers import LSTM
from keras.layers import CuDNNLSTM
from keras.layers.normalization import BatchNormalization
from keras.models import Model
from keras.callbacks import ModelCheckpoint

from keras import regularizers
from keras import backend as K
from keras.engine.topology import Layer
from keras import initializers, regularizers, constraints

import matplotlib.pyplot as plt
import seaborn as sns
from nltk.corpus import stopwords
from nltk.util import ngrams
from sklearn.feature_extraction.text import CountVectorizer
from collections import defaultdict
from collections import  Counter
plt
