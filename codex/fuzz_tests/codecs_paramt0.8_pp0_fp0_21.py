import codecs
codecs.register_error('ignore_surrogate', ignore_surrogate)
from warnings import warn
import MySQLdb
from collections import defaultdict
from dateutil.relativedelta import *
from data_extractor import *
from stats_extractor import *

from datetime import date
from datetime import datetime, timedelta

from tqdm import tqdm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import re
from sklearn.feature_extraction.text import CountVectorizer

import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

#Loading the data

#test_data = pd.read_csv("/Users/abhishekchaudhary/Downloads/test.csv")
#train_data = pd.read_csv("/Users/abhishekchaudhary/Downloads/train.csv")

test
