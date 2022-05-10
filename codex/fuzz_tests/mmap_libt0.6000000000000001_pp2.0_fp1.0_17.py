import mmap

from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
from nltk.corpus import wordnet
from nltk import pos_tag
from nltk.corpus import wordnet
from nltk.wsd import lesk
from nltk.corpus import wordnet_ic
from nltk.corpus import genesis
from nltk.corpus import brown
from nltk.corpus import wordnet_ic
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
from nltk.metrics.scores import (accuracy, precision, recall)
from nltk.classify import NaiveBayesClassifier
