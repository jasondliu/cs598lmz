import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)


# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
sns.set_style('whitegrid')


# ## 1. Load data

# In[5]:


df = pd.read_csv('data/Cancer_data.csv')
df.head()


# In[6]:


df.info()


# In[7]:


df.describe()


# ## 2. Preprocess

# In[8]:


# remove na
df = df.dropna()


# In[9]:


df.info()


# In[10]:


# remove unneccessary columns
df = df.drop(['id','Unnamed: 32'], axis=1)


# In[11]:


df.head()


# In[12]:


# convert label to nominal

