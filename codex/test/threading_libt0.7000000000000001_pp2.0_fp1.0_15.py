import threading
threading.stack_size(2**27)
import sys
import tensorflow as tf
import numpy as np
import types
import time
from keras.layers import Bidirectional, TimeDistributed, Dense, LSTM, Input, Activation, dot, concatenate, Embedding
from keras.models import Sequential, Model
from keras.optimizers import SGD, Adam, RMSprop
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
import keras.backend as K
import os
import pickle
import nltk
import re
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
import numpy as np
from numpy import newaxis
import pandas as pd
from collections import Counter
from collections import defaultdict
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import MinMaxScaler

