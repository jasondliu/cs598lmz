import bz2
bz2_file = bz2.BZ2File('data/train.ft.txt.bz2')
data = []
for line in bz2_file:
    data.append(line)
print(data[1])

import pandas as pd
df = pd.read_csv('data/train.csv', encoding='utf-8')
df.head()

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv('data/train.csv', encoding='utf-8')
df.head()

df.dropna(inplace=True)

blanks = []
for i, lb, rv in df.itertuples():
    if type(rv) == str:
        if rv.isspace():
            blanks.append(i)

df.drop(blanks,
