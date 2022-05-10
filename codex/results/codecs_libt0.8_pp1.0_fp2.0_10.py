import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# General libraries.
import os
import glob
import re
import json
import csv
import random
import math
import time
import datetime
from collections import Counter
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
import scipy
import numpy as np

# NLP libraries.
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer

# Sklearn libraries.
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import TruncatedSVD
from sklearn.naive_bayes import MultinomialNB
from
