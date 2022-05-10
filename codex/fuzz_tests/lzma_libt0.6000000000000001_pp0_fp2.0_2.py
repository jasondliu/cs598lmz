import lzma
lzma.LZMADecompressor().decompress(x)

# In[23]:


with open('test.png', 'wb') as f:
    f.write(lzma.LZMADecompressor().decompress(x))

# In[24]:


from PIL import Image
Image.open('test.png')

# In[25]:


import bz2
bz2.BZ2Decompressor().decompress(x)

# In[26]:


with open('test.png', 'wb') as f:
    f.write(bz2.BZ2Decompressor().decompress(x))

# In[27]:


Image.open('test.png')

# In[28]:


import zlib
zlib.decompress(x)

# In[29]:


with open('test.png', 'wb') as f:
    f.write(zlib.decompress(x))

# In[30]:


Image.open('test.png')

