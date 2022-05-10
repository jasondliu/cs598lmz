from lzma import LZMADecompressor
LZMADecompressor().decompress(open('data/test_lzma.xz', 'rb').read())

# In[ ]:


import gzip, bz2
print(gzip.decompress(open('data/test_gzip.gz', 'rb').read()))
print(bz2.decompress(open('data/test_bz2.bz2', 'rb').read()))

# In[ ]:


import zlib
zlib.decompress(open('data/test_zlib.zlib', 'rb').read())

# In[ ]:


import lzma
lzma.decompress(open('data/test_lzma.lzma', 'rb').read())

# In[ ]:


import lzma
lzma.decompress(open('data/test_lzma.xz', 'rb').read())

# In[ ]:


import lzma
lzma.decompress(open('data/test_lzma.xz', 'rb').read())

