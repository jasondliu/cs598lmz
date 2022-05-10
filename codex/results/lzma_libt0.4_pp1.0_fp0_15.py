import lzma
lzma.decompress(lzma.compress(b'Hello world!'))

# In[ ]:


import zlib
zlib.decompress(zlib.compress(b'Hello world!'))

# In[ ]:


import bz2
bz2.decompress(bz2.compress(b'Hello world!'))

# In[ ]:


import snappy
snappy.decompress(snappy.compress(b'Hello world!'))

# In[ ]:


import lz4
lz4.decompress(lz4.compress(b'Hello world!'))

# In[ ]:


import brotli
brotli.decompress(brotli.compress(b'Hello world!'))

# In[ ]:


import zstd
zstd.decompress(zstd.compress(b'Hello world!'))

# In[ ]:


import xxhash
xxhash.xxh32(b'Hello world!').digest()

# In[ ]
