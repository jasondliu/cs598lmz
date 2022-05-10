from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.read())


# In[ ]:


import gzip
with gzip.open('data/t10k-labels-idx1-ubyte.gz', 'rb') as f:
    file_content = f.read()
    
file_content[:4]


# In[ ]:


import gzip
with gzip.open('data/t10k-labels-idx1-ubyte.gz', 'rb') as f:
    file_content = f.read()

type(file_content) 


# In[ ]:


import struct

msb, = struct.unpack('>H', file_content[0:2])
print(msb)


# In[ ]:


msb


# In[ ]:


struct.unpack('>BBBB', file_content[2:6])


# In[ ]:


struct.unpack('>I', file_content[:4])


# In[ ]:


struct.calcsize('>I')
