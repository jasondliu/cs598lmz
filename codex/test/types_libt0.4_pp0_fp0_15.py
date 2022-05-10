import types
types.ModuleType('pandas')

#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#%%
df = pd.read_csv('train.csv')

#%%
df.head()

#%%
df.info()

#%%
df.describe()

#%%
df.columns

#%%
df.isnull().sum()

#%%
df.isnull().sum()/df.shape[0]

#%%
df.drop(['Cabin'], axis=1, inplace=True)

#%%
df.dropna(inplace=True)

#%%
df.isnull().sum()

#%%
df.head()

#%%
df['Survived'].value_counts()

#%%
sns.countplot(x='Survived', data=df)

#%%
sns.countplot(x='Survived', hue='Sex', data=df)

#%%
sns
