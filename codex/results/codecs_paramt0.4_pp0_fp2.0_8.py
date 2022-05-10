import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

import sys
import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize

stemmer = SnowballStemmer('english')

def preprocess(line):
    #line = line.replace('\n', ' ').replace('\r', ' ')
    line = line.lower()
    line = re.sub(r'[^\x00-\x7f]',r' ',line)
    line = re.sub(r'\d+', ' ', line)
    line = re.sub(r'\s+', ' ', line)
    line = re.sub(r'[^\w\s]',' ',line)
    line = line.strip()
    return line

def tokenize(line):
    tokens = word_tokenize(line)
    return tokens

def remove_stop_words(tokens):
    stop
