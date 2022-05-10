import bz2
bz2.BZ2File(path).read()

# In[ ]:


import gzip
gzip.open(path).read()

# In[ ]:


import lzma
lzma.open(path).read()

# In[ ]:


with gzip.open(path, 'rt') as f:
    text = f.read()
text


# In[ ]:


import bz2
with bz2.open(path, 'rt') as f:
    text = f.read()
text


# In[ ]:


import lzma
with lzma.open(path, 'rt') as f:
    text = f.read()
text


# ## 7.2 Reading Binary Data into a Mutable Buffer

# In[ ]:


import os
path = 'usagov_bitly_data2012-03-16-1331923249.txt'
os.path.getsize(path)


# In[ ]:


with open(path, 'rb') as f:
    record = f.read
