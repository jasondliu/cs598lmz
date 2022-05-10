import bz2
bz2_comp = bz2.BZ2Compressor()
compressed_data = bz2_comp.compress(data)
decompressed_data = bz2_comp.flush()
print(compressed_data)
print(decompressed_data)


# In[6]:


# using bz2 module's compress function
import bz2
bz2_comp = bz2.compress(data)
print(bz2_comp)


# In[7]:


# using bz2 module's decompress function
import bz2
bz2_comp = bz2.decompress(compressed_data)
print(bz2_comp)


# In[8]:


# using zlib module's compress function
import zlib
zlib_comp = zlib.compress(data)
print(zlib_comp)


# In[9]:


# using zlib module's decompress function
import zlib
zlib_comp = zlib.decompress(compressed_data)
print(zlib_comp)
