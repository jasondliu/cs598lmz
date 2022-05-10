import lzma
lzma.decompress(lzma.compress(b'Hello world!'))

# In[ ]:


import zlib
zlib.decompress(zlib.compress(b'Hello world!'))

# In[ ]:


import bz2
bz2.decompress(bz2.compress(b'Hello world!'))

# In[ ]:


