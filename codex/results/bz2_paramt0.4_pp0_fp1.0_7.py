from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('data/train.csv.bz2', 'rb').read())

#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#%%
df = pd.read_csv('data/train.csv', nrows=10_000_000)
df.head()

#%%
df.describe()

#%%
df.info()

#%%
df.isna().sum()

#%%
df.dropna(inplace=True)

#%%
df.info()

#%%
df.describe()

#%%
df.head()

#%%
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])

#%%
df.head()

#%%
df['pickup_datetime'].dt.year.value_counts()

#%%
df['pickup_datetime'].dt.month.value_counts()

#%%
