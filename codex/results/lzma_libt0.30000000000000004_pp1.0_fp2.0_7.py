import lzma
lzma.decompress(open('data/raw/train.csv.xz', 'rb').read())

# %%
import pandas as pd
df = pd.read_csv('data/raw/train.csv')
df.head()

# %%
df.shape

# %%
df.info()

# %%
df.describe()

# %%
df.dtypes

# %%
df.columns

# %%
df.isnull().sum()

# %%
df.isnull().sum().sum()

# %%
df.isnull().sum() / df.shape[0]

# %%
df.isnull().sum() / df.shape[0] * 100

# %%
df.isnull().sum() / df.shape[0] * 100

# %%
df.isnull().sum() / df.shape[0] * 100

# %%
df.isnull().sum() / df.shape[0] * 100

# %%
df.isnull().sum() / df.shape[0] * 100


