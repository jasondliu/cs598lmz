from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# In[ ]:


import lzma
with lzma.open('/content/drive/My Drive/Colab Notebooks/data/data.csv.xz') as f:
    file_content = f.read()

# In[ ]:


import pandas as pd
df = pd.read_csv(io.BytesIO(file_content))

# In[ ]:


df.head()

# In[ ]:


df.shape

# In[ ]:


df.info()

# In[ ]:


df.describe()

# In[ ]:


df.columns

# In[ ]:


df.isnull().sum()

# In[ ]:


df.isnull().sum().sum()

# In[ ]:


df.isnull().sum()/df.shape[0]

# In[ ]:


df.isnull().sum()/df.shape[0]*100

# In[ ]:


df.is
