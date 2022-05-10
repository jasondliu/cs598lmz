import codecs
codecs.register_error('replace_with_space', repl_with_space)
import nltk
import string
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import xgboost as xgb
from joblib import Parallel, delayed
import multiprocessing
num_cores = multiprocessing.cpu_count()
#import multiprocessing
#num_cores = multiprocessing.cpu_count()

def preprocess_string(s):
    punct = '''.,!?:-()[]{}\\"'/@#$%^&*_~'''
    translator = str.maketrans(dict.fromkeys(punct, " "))
    s = s.translate(translator)
    return s


def _preprocess_string(s):
    s = s.decode('utf8', errors='replace_with_space')
    s = preprocess_
