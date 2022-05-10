import mmap
import nltk
import re
import sys
import time
import tqdm
import uuid
import warnings
from collections import defaultdict
from datetime import datetime
from itertools import repeat, chain
from multiprocessing import Pool
from sys import getsizeof
from time import time
from urllib.parse import urlparse

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from scipy.sparse import coo_matrix, hstack, vstack
from sklearn.base import BaseEstimator, TransformerMixin, ClassifierMixin, clone
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier, GradientBoostingRegressor, \
    RandomForestRegressor
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

