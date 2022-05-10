import gc, weakref
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder

import lightgbm as lgb

import os
print(os.listdir("../input"))

# Any results you write to the current directory are saved as output.

# In[ ]:


train = pd.read_csv('../input/train.csv')
test = pd.read_csv('../input/test.csv')

# In[ ]:


train.head()

# In[ ]:


test.head()

# In[ ]:


train.info()

# In[ ]:


test.info()

# In[ ]:


train.isnull().sum()

# In[ ]:


test.isnull().sum()

# In
