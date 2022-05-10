from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# In[ ]:


# bz2.open()
import bz2
with bz2.open('sample.bz2', 'rt') as f:
    for line in f:
        print(line)

# In[ ]:


# The compress() and decompress() functions of the zlib module provide a simple interface to compress and decompress data.
import zlib, gzip
s = b'witch which has which witches wrist watch'
len(s)

# In[ ]:


t = zlib.compress(s)
len(t)

# In[ ]:


zlib.decompress(t)

# In[ ]:


zlib.crc32(s)

# In[ ]:


# The gzip module provides a more complete interface for creating and reading gzip-compressed files.
import gzip
f = gzip.open('sample.gz', 'wt')
f.write('Hello world!')
f.close()

# In[ ]:


f = gzip
