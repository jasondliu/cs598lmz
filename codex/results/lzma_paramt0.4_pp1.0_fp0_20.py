from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# In[ ]:


import zlib
zlib.decompress(data, -zlib.MAX_WBITS)

# In[ ]:


import bz2
bz2.decompress(data)

# In[ ]:


import brotli
brotli.decompress(data)

# In[ ]:


import lz4.block
lz4.block.decompress(data)

# In[ ]:


import lz4.frame
lz4.frame.decompress(data)

# In[ ]:


import lz4.legacy
lz4.legacy.decompress(data)

# In[ ]:


import zstandard
zstandard.ZstdDecompressor().decompress(data)

# In[ ]:


import blosc
blosc.decompress(data)

# In[ ]:


import snappy
snappy.decompress(data)

# In[ ]:


import z
