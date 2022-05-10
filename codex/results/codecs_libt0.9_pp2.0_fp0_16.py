import codecs
codecs.register(lambda name: codecs.lookup('utf8')
if name == 'cp65001' else None)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
import seaborn as sns
import scipy

df=pd.read_csv("C:\Users\sojoe\Desktop\데이터분석과정\Github\R_ML_Python\data\boston.csv")
print(df.head())
print(df.columns)
print(df.info())
print(df.describe())


del df['Unnamed: 0']
df.head(10)
df.tail(10)
df.info()
df.describe()

type(df)
df.shape
df.shape[0]
df.shape[1]

df.size

df.values
df.columns
df.index

df.dtypes

df['CRIM'].head()
df['MEDV'
