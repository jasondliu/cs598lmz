from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# In[ ]:


# 1.3.3 Reading from a Compressed File (Gzip)
import gzip
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

# In[ ]:


# 1.3.4 Writing to a Compressed File (Bz2)
import bz2
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()

# In[ ]:


# 1.3.5 Reading Compressed Data in Chunks
import gzip
f = gzip.open('somefile.gz', 'rt')
f.read(10)

# In[ ]:


# 1.3.6 Working with ZIP Archives
import zipfile
with zipfile.ZipFile
