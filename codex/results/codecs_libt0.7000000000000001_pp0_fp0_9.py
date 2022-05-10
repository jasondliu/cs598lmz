import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import string
import sys
import os
import re
import random
import argparse
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize,word_tokenize
import pandas as pd
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.collocations import *
import csv
import numpy as np
from numpy.random import seed
from numpy.random import randint
from scipy.stats import norm
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import random
import itertools
import math
import pysam
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVector
