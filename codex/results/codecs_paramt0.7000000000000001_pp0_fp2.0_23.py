import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

import numpy as np
import pandas as pd
import gensim
import gensim.models.word2vec as w2v
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import multiprocessing
import os
import sys
import re
import string
import nltk
from nltk.corpus import stopwords
import logging

stop = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^a-zA-Z0-9_\s]', '', text)
    # Replace newlines
    text = text.replace('\n', ' ')
    text = text.replace('\r', ' ')
    # Replace multiple whitespace with a single space
    text = re.sub('\s+', ' ', text)
    # Remove numbers
    text = re.sub('\d+',
