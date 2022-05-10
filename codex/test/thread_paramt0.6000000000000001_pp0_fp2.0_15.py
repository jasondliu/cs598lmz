import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

#%%
from os.path import join
import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import KFold

from keras.models import Model
from keras.layers import Input, Dense, Embedding, SpatialDropout1D, concatenate
from keras.layers import GRU, Bidirectional, GlobalAveragePooling1D, GlobalMaxPooling1D
from keras.preprocessing import text, sequence
from keras.callbacks import Callback

from sklearn.metrics import roc_auc_score
import re, string
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

from keras import backend as K
from keras.engine.topology import Layer
from keras import initializers, regularizers, constraints

from gensim.models import KeyedVectors
from sklearn.metrics import accuracy_score

#%%
