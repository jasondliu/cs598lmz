from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# In[ ]:


import bz2
bz2.decompress(data)

# In[ ]:


import zlib
zlib.decompress(data)

# In[ ]:


import gzip
gzip.decompress(data)

# In[ ]:


import zipfile
zipfile.ZipFile('data.zip').extractall()

# In[ ]:


import tarfile
tarfile.open('data.tar.gz').extractall()

# In[ ]:


import tarfile
tarfile.open('data.tar.bz2').extractall()

# In[ ]:


import tarfile
tarfile.open('data.tar.xz').extractall()

# In[ ]:


import tarfile
tarfile.open('data.tar.lzma').extractall()

# In[ ]:


import tarfile
tarfile.open('data.tar.zst').extractall()

# In[ ]:


