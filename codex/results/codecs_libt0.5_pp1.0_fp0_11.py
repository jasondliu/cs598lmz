import codecs
codecs.open('books/' + bookname, encoding='utf-8').read()

#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline
#%config InlineBackend.figure_format = 'retina'

import seaborn as sns
sns.set_context("poster")
sns.set_style("white")

#%%
df = pd.read_csv('books/' + bookname,header=None)
df.columns = ['word']
df.head()

#%%
df['word'] = df['word'].str.lower()
df.head()

#%%
df.shape

#%%
df['word'].value_counts()

#%%
df_words = df['word'].value_counts()
df_words.head()

#%%
df_words.shape

#%%
df_words.index

#%%
df_words.index[0]

#%%
df_words.values
