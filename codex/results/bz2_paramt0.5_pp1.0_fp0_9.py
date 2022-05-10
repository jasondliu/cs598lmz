from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(f.read(100))

# In[ ]:


import bz2
bz2.decompress(f.read(100))

# In[ ]:


f.seek(0)

# In[ ]:


import gzip
gzip.open(f, 'rb').read(100)

# In[ ]:


f.seek(0)

# In[ ]:


import lzma
lzma.open(f, 'rb').read(100)

# In[ ]:


f.seek(0)

# In[ ]:


import lzma
lzma.open(f, 'rb').read(100)

# In[ ]:


f.seek(0)

# In[ ]:


import lzma
lzma.open(f, 'rb').read(100)

# In[ ]:


f.seek(0)

# In[ ]:


import lzma
lzma.open(f, 'rb').read(100
