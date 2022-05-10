import codecs
codecs.register_error('replace_with_space', codecs.lookup_error('ignore'), lambda e: (u' ', e.start + 1))

from numpy import *
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer
from math import log
from nltk.tokenize import RegexpTokenizer
import nltk
from nltk.corpus import wordnet
import re, string
from nltk.stem import SnowballStemmer


def getStopwords():
    stopwords = []
    f = open('stopwords.txt', 'r')
    reader = csv.reader(f, delimiter='\n')
    for row in reader:
        stopwords.append(row[0])
    return stopwords

def getTagPairs():
    tags =[]
    f = open('tags.txt', 'r')
    reader = csv.reader
