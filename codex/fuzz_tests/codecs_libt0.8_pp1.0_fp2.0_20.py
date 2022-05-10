import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

import requests
from bs4 import BeautifulSoup
import collections
import lxml.builder

#import nltk
#nltk.download()
#from nltk.corpus import wordnet as wn

import os
  
total_count = 0

def normalize(word):
    return word.lower()

def is_valid_word(word):
    return word.isalpha()

def write_summary(html_out, words_dict, title):
    E = lxml.builder.ElementMaker()
    html_root = E.html(
        E.head(
            E.meta(name="Generator", content="giraffe"),
            E.meta(http-equiv="Content-Type", content="text/html"),
            E.title(title)),
        E.body(
            *[E.div(str(k), " ", str(v),"<br>") for k, v in words_dict.iteritems
