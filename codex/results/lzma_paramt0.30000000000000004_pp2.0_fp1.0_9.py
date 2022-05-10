from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# In[ ]:


#Decompress the data
import lzma
with lzma.open('data/train.csv.xz') as f:
    file_content = f.read()

# In[ ]:


#Read the data
import pandas as pd
df = pd.read_csv(io.StringIO(file_content.decode('utf-8')))

# In[ ]:


#Check the data
df.head()

# In[ ]:


#Check the data
df.tail()

# In[ ]:


#Check the data
df.info()

# In[ ]:


#Check the data
df.describe()

# In[ ]:


#Check the data
df.describe(include=['O'])

# In[ ]:


#Check the data
df[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean().sort_values(by='Survived', ascending=False)
