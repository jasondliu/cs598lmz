import ctypes
ctypes.cast(0, ctypes.py_object)

# %%
import pandas as pd

columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
df = pd.read_csv('adult.data', header=None, names=columns)

# %%
df.head()

# %%
df.info()

# %%
df.describe()

# %%
df.income.value_counts()

# %%
df.income.value_counts(normalize=True)

# %%
df.education.value_counts()

# %%
df.occupation.value_counts()

# %%
df.income.value_counts()

# %%
df.income.value_counts(normalize=True)

# %%
df.education.value_counts()

# %%
