import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%

import numpy as np
import pandas as pd

#%%

df = pd.DataFrame(np.random.randn(10, 5))
df.head()

#%%

df.to_csv('foo.csv')

#%%

pd.read_csv('foo.csv').head()

#%%

df.to_hdf('foo.h5', 'df')

#%%

pd.read_hdf('foo.h5', 'df').head()

#%%

df.to_excel('foo.xlsx', sheet_name='Sheet1')

#%%

pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA']).head()

#%%

df.to_sql('foo', 'sqlite:///foo.db')

#%%

pd.read_sql('foo', 'sqlite:///foo.db').head()


