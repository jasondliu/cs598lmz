import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

import utils
import extract_pii_regexes
import ner_course
import extract_atts
import copy
import numpy as np
from nltk import ngrams
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.collocations import *
import math
import random
import extract_ngrams
import matplotlib.pyplot as plt
import pandas as pd
import extract_pii_subs

lemmatizer = WordNetLemmatizer()

# constants
index = 'li'
index_with_type = 'li'

read_file_list = [
    'anand_nagar.json',
    'beed_bypass.
