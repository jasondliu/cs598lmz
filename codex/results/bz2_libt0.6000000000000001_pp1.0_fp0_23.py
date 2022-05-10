import bz2
bz2.__version__

# In[5]:


import numpy as np
np.__version__


# In[6]:


import pandas as pd
pd.__version__


# In[7]:


import sklearn
sklearn.__version__


# In[8]:


import matplotlib
matplotlib.__version__


# In[9]:


import csv
import math
import os
import sys

get_ipython().run_line_magic('matplotlib', 'inline')

from sklearn.model_selection import train_test_split


# In[10]:


# function to load data from a csv file
def load_data(file_name, debug = False):
    data = np.genfromtxt(file_name, delimiter=',', dtype=None, encoding='utf-8')
    if debug:
        print('Shape of loaded data:', data.shape)
    return data


# In[11]:


# function to load data from a bz2 file
def load_data_bz
