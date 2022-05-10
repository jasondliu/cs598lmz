import codecs
codecs.register_error("strict", codecs.ignore_errors)
import os
import sys
import re
import random
import string
import unicodedata
import numpy as np
import copy

# For loading and preprocessing data
import cPickle as pkl
from collections import OrderedDict
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.util import ngrams
import json

# For training and evaluation
from keras.preprocessing import sequence
from keras.utils import np_utils
from keras.models import Sequential, Model
from keras.layers import Dense, Dropout, Activation, Embedding, Flatten, Input, Merge, Convolution1D, MaxPooling1D, GlobalMaxPooling1D, LSTM, GRU, Bidirectional, TimeDistributed, Reshape, Permute, Lambda, RepeatVector
from keras.layers.merge import Add
