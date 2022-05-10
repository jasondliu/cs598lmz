import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

import sys
sys.path.append(r'../')

import pandas as pd
from ast import literal_eval
from tqdm import tqdm
import os
from gensim.models import Word2Vec
import numpy as np

from model.utils import *
from model.utils_sklearn import *
from model.utils_gensim import *
from model.utils_keras import *
from model.utils_torch import *

from sklearn.preprocessing import OneHotEncoder

class text_embedding(object):
    def __init__(self, size = 100, window = 3, min_count = 5, sample = 1e-3, hs = 0, negative = 5, cbow = 0, sg = 1, iter = 5, workers = 4, **kwargs):
        self.size = size
        self.window = window
        self.min_count = min_count
        self.sample = sample
        self.
