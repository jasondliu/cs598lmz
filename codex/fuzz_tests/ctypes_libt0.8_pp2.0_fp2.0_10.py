import ctypes
ctypes.cdll.LoadLibrary('/Users/chris/anaconda/lib/python3.6/site-packages/libmkl_intel_thread.dylib')
ctypes.cdll.LoadLibrary('/Users/chris/anaconda/lib/python3.6/site-packages/libiomp5.dylib')

import pandas as pd
df = pd.read_csv("../data/processed/train_engineered.csv", index_col=0, header=0)

import numpy as np
train = df.iloc[:, 1:]
test = df.iloc[:, 0:1]

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(train, test)

print(lm.coef_)
print(lm.intercept_)

coefficients = pd.DataFrame(lm.coef_, train.columns)
coefficients.columns = ["coefficients"]
coefficients.sort_values(by="coefficients", ascending=False)

def rmse
