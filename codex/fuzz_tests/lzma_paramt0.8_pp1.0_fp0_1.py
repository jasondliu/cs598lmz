from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
assert LZMADecompressor().decompress(data).decode('utf-8') == s


# In[ ]:


import zlib
data = zlib.compress(s.encode('utf-8'))
print(data)


# In[ ]:


zlib.decompress(data)
assert zlib.decompress(data).decode('utf-8') == s


# In[ ]:


# 1.1.1

from bz2 import BZ2Compressor
from bz2 import BZ2Decompressor

bz2comp = BZ2Compressor()
data = bz2comp.compress(s.encode('utf-8')) + bz2comp.flush()
print(data)


# In[ ]:


bz2decomp = BZ2Decompressor()
bz2decomp.decompress(data)
assert bz2decomp.decompress(data).decode('utf-8') == s


# In[ ]
