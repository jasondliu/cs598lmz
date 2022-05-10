import mmap
import codecs
import re
import glob
import os
import sys
import operator
from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation
import string
import nltk
from nltk.stem.porter import PorterStemmer
import numpy as np
import csv
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse
import nltk
from nltk.corpus import wordnet
from nltk.corpus import wordnet_ic
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
