import gc, weakref
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import LabelEncoder

import lightgbm as lgb

import warnings
warnings.filterwarnings('ignore')

gc.enable()

# Any results you write to the current directory are saved as output.

# In[ ]:


train_df = pd.read_csv('../input/train.csv')
test_df = pd.read_csv('../input/test.csv')

# In[ ]:


train_df.head()

# In[ ]:


test_df.head()

# In[ ]:


train_df.shape

# In[ ]:


test_df.shape

# In[ ]:


train_df.isnull().sum()

# In[ ]:


test_df.isnull().
