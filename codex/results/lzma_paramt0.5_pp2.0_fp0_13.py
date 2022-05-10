from lzma import LZMADecompressor
LZMADecompressor().decompress(b)

# In[9]:


import os
import pandas as pd
import numpy as np

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.models import load_model

import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

# In[10]:


df = pd.read_csv('data/creditcard.csv')

# In[11]:


df.head()

# In[12]:


df.describe()

# In[13]:


df.info()

# In[14]:


df.isna().sum()

# In
