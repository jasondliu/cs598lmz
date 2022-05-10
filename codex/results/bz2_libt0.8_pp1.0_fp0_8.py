import bz2
bz2.decompress(raw)

#%%
import numpy as np
import pandas as pd

data = pd.read_csv('data/jamesbond.csv', index_col='Film')
data.sort_index(inplace=True)
data

data['Year'] >= 1960

data.loc[data['Year'] >= 1960]

#%%
data.loc[(data['Year'] >= 1960) & (data['Box Office'] > 800)]

#%%
data.loc[(data['Year'] >= 1960) & (data['Box Office'] > 800), ['Actor', 'Director']]

#%%
data.iloc[15]

#%%
data.iloc[[15, 20]]

#%%
data.iloc[15:20]

#%%
data.loc['Goldfinger']

#%%
data.iloc[[5, 10, 15, 20]]

#%%
data.iloc[:4]

#%%
data.iloc[4:8]

#%%
data.iloc[20:]
