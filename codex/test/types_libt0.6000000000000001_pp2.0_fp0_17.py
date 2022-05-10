import types
types.SimpleNamespace

# %%
import pandas as pd

# %%
df = pd.read_csv('../data/dummy.csv', index_col='ID')

# %%
df.head()

# %%
df.shape

# %%
df.dtypes

# %%
df.describe()

# %%
df.columns

# %%
df.index

# %%
df.info()

# %%
df.isna()

# %%
df.isna().sum()

# %%
df.isna().sum().sum()

# %%
df['Age'].isna().sum()

# %%
df['Age'].isna().sum()/df.shape[0]

# %%
df['Age'].isna().sum()/df.shape[0]*100

# %%
df['Age'].isna().sum()/df.shape[0]*100

# %%
df.dropna(inplace=True)

# %%
df.shape

# %%
