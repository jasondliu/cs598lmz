import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)
%matplotlib inline

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import collections

import tweepy as tw
import nltk
from nltk.corpus import stopwords
import re
import networkx

import warnings
warnings.filterwarnings("ignore")

sns.set(font_scale=1.5)
sns.set_style("whitegrid")
consumer_key= 'NJPZ7J9gjfTzTcqI3NitLBiQg'
consumer_secret= 'tJHNSQZQ2XOv9rBVkdzJGtRjhZM0luZFwNoa5h5jKx5XkXvz8W'
access_token= '1166672842635601921-hNgEu1RYKBz1vQECWJ3
