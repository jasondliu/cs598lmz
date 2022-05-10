import codecs
codecs.register_error('strict', codecs.ignore_errors)

import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder

from keras.models import Model
from keras.layers import Dense, Input, Dropout, LSTM, Activation
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.initializers import glorot_uniform
from keras.utils.np_utils import to_categorical
from keras.callbacks import ModelCheckpoint

from keras.models import model_from_json

from keras import backend as K

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

from nltk.stem import WordNetLemmatizer

from keras.layers import Dense, Input, LSTM, Embedding, Dropout, Activation
from keras.l
