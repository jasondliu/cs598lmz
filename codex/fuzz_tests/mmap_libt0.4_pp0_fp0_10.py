import mmap
import time
import os
import sys
import pickle
import re
import numpy as np
import tensorflow as tf
import math
import random
from tensorflow.contrib.tensorboard.plugins import projector
import gensim
from gensim.models import Word2Vec
from gensim.models.keyedvectors import KeyedVectors
from gensim.test.utils import get_tmpfile
from gensim.scripts.glove2word2vec import glove2word2vec

# import matplotlib
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt

# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer
# from nltk.stem.porter import PorterStemmer

# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.metrics import f1_score
# from sklearn.metrics import precision_score
# from
