from lzma import LZMADecompressor
LZMADecompressor().decompress(open('../data/train.csv.xz', 'rb').read())

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df = pd.read_csv('../data/train.csv')
df.head()

# %%
df.describe()

# %%
df.info()

# %%
df.isnull().sum()

# %%
df.columns

# %%
df['Survived'].value_counts()

# %%
sns.countplot(x='Survived', data=df)

# %%
sns.countplot(x='Survived', hue='Sex', data=df)

# %%
sns.countplot(x='Survived', hue='Pclass', data=df)

# %%
df['Age'].plot.hist()

# %%
df['Fare'].plot.hist(bins=20, figsize=(10, 5))

# %%
df
