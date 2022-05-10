from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.BZ2File('data/train.ft.txt.bz2').read())

#%%
import pandas as pd
import numpy as np

df = pd.read_csv('data/train.csv')
df.head()

#%%
df.shape

#%%
df.isnull().sum()

#%%
df.isnull().sum() / df.shape[0]

#%%
df.dropna(inplace=True)

#%%
df.isnull().sum()

#%%
df.shape

#%%
df.drop_duplicates(inplace=True)
df.shape

#%%
df.drop(columns=['id', 'keyword', 'location'], inplace=True)
df.head()

#%%
df['target'].value_counts()

#%%
df['target'].value_counts(normalize=True)

#%%
df['target'].value_counts().plot.bar()

#%%
df
