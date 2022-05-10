import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#%%
# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re
import sys
import time
import datetime
import pickle
import gc
import warnings
warnings.filterwarnings('ignore')

#%%
# import data
df_train = pd.read_csv('../input/train.csv')
df_test = pd.read_csv('../input/test.csv')

#%%
# check data
print('train data shape:', df_train.shape)
print('test data shape:', df_test.shape)

#%%
# check data
df_train.head()

#%%
# check data
df_test.head()

#%%
# check data
df_train.info()

#%%
# check data
df_test.info()

#%%
# check data

