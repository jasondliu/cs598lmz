import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

#%%
os.chdir('C:/Users/User/Desktop/Data Science/Projects/Titanic')

#%%
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

#%%
train.head()

#%%
train.info()

#%%
train.describe()

#%%
train.isnull().sum()

#%%
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')

#%%
sns.set_style('whitegrid')
sns.countplot(x='Survived',data=train,palette='RdBu_r')

#%%
sns.set_style('whitegrid')
