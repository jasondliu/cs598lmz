import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import nltk
from nltk.corpus import stopwords
import string
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

%matplotlib inline

eng_stopwords = set(stopwords.words("english"))
pd.options.mode.chained_assignment = None

train = pd.read_csv("../input/train.csv")
test = pd.read_csv("../input/test.csv")

print(train.shape)
print(test.shape)

train.head()

train.isnull().sum()

def clean(comment):
    comment = comment.lower()
    comment = re.sub("\\n","",comment)
    comment = re.sub("\d{1,3}\.\d{1,
