import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

import csv
import json
import re
import string
import sys

from HTMLParser import HTMLParser
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
from nltk.tokenize import TweetTokenizer
from treelib import Node, Tree

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def normalize_word(word):
    word = word.strip().lower()
    word = word.replace(u'\u2019', "'")
    # word = word.translate(string.maketrans("",""), string.punctuation)
    word = word.translate(string.maketrans("",""), string.punctuation.replace('#', ''))

    if is_number(word):
        return '<N>'
    else:
        return word


def get_all_words(data):
    all_words =
