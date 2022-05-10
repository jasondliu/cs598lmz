import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

#%%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#%%

df = pd.read_csv('../data/raw/data.csv')

#%%

df.head()

#%%

df.columns

#%%

df.shape

#%%

df.describe()

#%%

df.info()

#%%

df.isnull().sum()

#%%

df.columns

#%%

df.drop(['Unnamed: 0', 'id', 'imdb_id', 'popularity', 'budget_adj', 'revenue_adj', 'homepage', 'keywords', 'overview', 'production_companies', 'vote_count', 'vote_average'], axis=1, inplace=True)

#%%

df.head()

#%%

df
