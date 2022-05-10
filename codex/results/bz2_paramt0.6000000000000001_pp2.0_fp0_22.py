from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('../data/train.csv.bz2').read())

#%%

import pandas as pd

train_df = pd.read_csv('../data/train.csv', index_col='id')
train_df.head()

#%%

train_df['question_text'].head()

#%%

train_df['target'].head()

#%%

train_df['target'].value_counts()

#%%

train_df['target'].value_counts().plot(kind='bar')

#%%

train_df['target'].value_counts().plot(kind='pie')

#%%

import seaborn as sns

sns.countplot(train_df['target'])

#%%

sns.countplot(train_df['target'], hue=train_df['target'])

#%%

sns.countplot(train_df['target'].map(lambda x: 'insincere' if x==1 else 'sincere
