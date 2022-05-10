import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)
import re
import os
import pickle
import numpy as np
from gensim.models import Word2Vec
from gensim.models.keyedvectors import KeyedVectors
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Model, Sequential
from keras.layers import Input, Concatenate, Dense, Reshape, Dropout, Embedding, LSTM, Bidirectional, Flatten, Convolution1D, MaxPooling1D, Convolution2D, MaxPooling2D, Activation, MaxoutDense, Lambda
from keras.optimizers import Adam
from keras import backend as K
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.regularizers import l2
