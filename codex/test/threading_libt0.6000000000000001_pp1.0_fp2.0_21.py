import threading
threading.Thread(target=lambda:subprocess.call(["python3","-m","http.server","8000"])).start()

# ## 1. What is the data?

# In[2]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

# ## 2. How is the data organized?

# In[3]:

# import the data

data = pd.read_csv('data.csv')
data.head()


# In[4]:

data.shape


# In[5]:

data.info()


# ## 3. What are the variables?

# In[6]:

data.columns


# ## 4. What are the observations?

# In[7]:

data.index


# ## 5. What was the most popular movie?

# In[8]:

data.sort_values(by='star_rating', ascending=False).head()


# In[9]:

data.sort_values
