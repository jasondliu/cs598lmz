import socket
socket.if_indextoname(3)

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set()

# In[ ]:


df = pd.read_csv('../input/train.csv')
df.head()

# In[ ]:


df.info()

# In[ ]:


df.describe()

# In[ ]:


df.isnull().sum()

# In[ ]:


df['Age'] = df['Age'].fillna(df['Age'].median())
df.isnull().sum()

# In[ ]:


df['Embarked'].value_counts()

# In[ ]:


df['Embarked'] = df['Embarked'].fillna('S')
df.isnull().sum()

# In[ ]:


df['Sex'] = df['Sex'].map
