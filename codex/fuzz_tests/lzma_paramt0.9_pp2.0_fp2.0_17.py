from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma.open("compressed.xz").read(10))


# In[9]:


import pickle
import gzip
bz2pickle_file = bz2.BZ2File("compressed.bz2", "rb")
gzip_file = gzip.open("compressed.gz", "rb")
lzma_file = lzma.open("compressed.xz", "rb")
pickle.load(bz2pickle_file)
pickle.load(gzip_file)
pickle.load(lzma_file)
# the formats are not compatible


# In[3]:


get_ipython().system('lzma --version 2>&1 | head -2')
print('lzma.version: {}'.format(lzma.version))


# In[5]:


bz2.version


# In[10]:


import bz2, gzip, lzma
def bz2_open(filename):
    return bz2.BZ2File(filename
