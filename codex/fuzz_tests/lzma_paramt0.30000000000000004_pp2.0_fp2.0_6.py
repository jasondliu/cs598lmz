from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# In[ ]:


#GZIP
import gzip
with gzip.open('file.txt.gz', 'rt') as f:
    text = f.read()

# In[ ]:


#BZIP2
import bz2
with bz2.open('file.txt.bz2', 'rt') as f:
    text = f.read()

# In[ ]:


#ZLIB
import zlib
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s)
len(t)
zlib.decompress(t)
zlib.crc32(s)

# In[ ]:


#TAR
import tarfile
with tarfile.open('example.tar', 'r') as t:
    t.extractall()
    t.close()

# In[ ]:


#ZIP
import zipfile
with zipfile.ZipFile('example.zip', 'r') as z:
    z.ext
