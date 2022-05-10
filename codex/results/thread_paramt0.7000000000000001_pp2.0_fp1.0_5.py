import sys, threading
threading.Thread(target=lambda: sys.stdout.flush()).start()
import time
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from sklearn.metrics import fbeta_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalMaxPooling1D
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint
from keras.models import load_model

import numpy as np

from preprocess import load_data, load_embedding_matrix, load_
