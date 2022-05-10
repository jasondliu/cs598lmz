import lzma
lzma.open("./data/train.csv.xz")

# %%
import pandas as pd
df = pd.read_csv("./data/train.csv.xz", nrows=100_000)
df.head()

# %%
df.info()

# %%
df.describe()

# %%
df.isna().sum()

# %%
df.isnull().sum()

# %%
df.dropna(inplace=True)

# %%
df.isna().sum()

# %%
df.isnull().sum()

# %%
df.describe()

# %%
df.groupby("Survived").mean()

# %%
df.dtypes

# %%
df.drop(['Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

# %%
df.head()

# %%
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df.head()

# %%
df['Embark
