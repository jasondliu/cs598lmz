import codecs
codecs.register_error('replace',lambda e: unicode(e.object[e.start:e.end], 'utf-8'), 'replace')
sys.setdefaultencoding = 'utf-8'
import glob
import string
import os
import re
import random
import nltk
import json
import numpy as np
from lxml.etree import ElementTree
import itertools
import json

def num_tokens(s):
    tkns = nltk.word_tokenize(s)
    return len(tkns)

def num_real_tokens(s):
    "Remove puncitation and stopwords"
    tkns = nltk.word_tokenize(s)
    tkns = [x for x in tkns if x not in string.punctuation + '``' + "''"]    
    tkns = [x for x in tkns if not x in ENGLISH_STOP_WORDS]
    return len(tkns)

def num_bigram(s):
    """Find all the bigrams in the text"""
