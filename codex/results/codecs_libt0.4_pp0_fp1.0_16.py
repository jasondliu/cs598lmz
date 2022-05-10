import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df = pd.read_csv('data/train.csv')

# %%
df.head()

# %%
df.describe()

# %%
df.info()

# %%
df.isna().sum()

# %%
df.columns

# %%
df.dtypes

# %%
df.shape

# %%
df.columns

# %%
df.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'], inplace=True)

# %%
df.head()

# %%
df.columns

# %%
df.dropna(inplace=True)

# %%
df.isna().sum()

# %%
df.shape

# %%
df.dtypes

