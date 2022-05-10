from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(data))

# In[54]:
cProfile.run('bz2.compress(data)')

# In[55]:
cProfile.run('BZ2Compressor().compress(data)')

# In[56]:
cProfile.run('bz2.decompress(bz2.compress(data))')

# In[57]:
cProfile.run('BZ2Decompressor().decompress(bz2.compress(data))')

# In[58]:
from zlib import decompress, MAX_WBITS
decompress(zlib.compress(data), -MAX_WBITS)

# In[59]:
cProfile.run('zlib.compress(data, 3)')

# In[60]:
cProfile.run('zlib.decompress(zlib.compress(data, 3), -MAX_WBITS)')

# In[61]:
from gzip import decompress as gzdecompress
gzdecompress(g
