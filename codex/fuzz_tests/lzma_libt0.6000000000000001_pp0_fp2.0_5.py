import lzma
lzma.LZMA_OK

#%%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%%

data_path = 'D:/Data/Kaggle/LANL/'

#%%

df_train = pd.read_csv(data_path + 'train.csv', dtype={'acoustic_data': np.int16, 'time_to_failure': np.float64})
df_test = pd.read_csv(data_path + 'test/test.csv', dtype={'acoustic_data': np.int16})

#%%

df_train.info()

#%%

df_train.shape

#%%

df_train.head(10)

#%%

df_train.describe()

#%%

df_train.isnull().values.any()

#%%

df_train.isnull().sum()

#%%

df_test.info()

#%%
