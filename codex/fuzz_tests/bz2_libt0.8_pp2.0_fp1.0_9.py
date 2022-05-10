import bz2
bz2.BZ2File(path+"data_01_test.json.bz2").read()

data = json.loads(bz2.BZ2File(path+"data_01_test.json.bz2").read())
data[1]

import pandas as pd

train = pd.read_json(path+"data_01_train.json")
test = pd.read_json(path+"data_01_test.json")

train[1] = train[1].astype('str')
train[2] = train[2].astype('str')
test[1] = test[1].astype('str')
test[2] = test[2].astype('str')

X = train[1] + " " + train[2]
y = train[0]
X_test = test[1] + " " + test[2]

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

X_train, X_val, y
