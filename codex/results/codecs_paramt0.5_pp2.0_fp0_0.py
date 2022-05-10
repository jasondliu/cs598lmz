import codecs
codecs.register_error('strict', codecs.ignore_errors)

import lxml.html
from lxml.html.clean import Cleaner
import re
import json

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer

import gensim
from gensim import corpora

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from collections import Counter

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def get_urls(file_path):
    with open(file_path, 'r') as f:
        urls = f.read().splitlines()
    return urls

def get_html(url):
    try:
        return requests.get(url).text
    except Exception as e:
        print(e)
        print('Could not get url:
