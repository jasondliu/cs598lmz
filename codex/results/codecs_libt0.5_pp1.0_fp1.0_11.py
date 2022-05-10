import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import TweetTokenizer
import os
import random
import tensorflow as tf
import tensorflow.contrib.keras as kr
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

import sys
sys.path.append('../')
import config

np.random.seed(42)

# 读取数据
df = pd.read_csv(config.DATA_PATH, encoding='utf-8')

# 清洗数据
df['comment_text'] = df['comment_text'].apply(lambda x: x.replace("\n", ""))
df['comment_text'] = df
