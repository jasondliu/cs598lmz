from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# In[ ]:


# lzma
import lzma
with lzma.open('data.xz', 'rb') as f:
    file_content = f.read()
    
# bz2
import bz2
with bz2.open('data.bz2', 'rb') as f:
    file_content = f.read()
    
# gzip
import gzip
with gzip.open('data.gz', 'rb') as f:
    file_content = f.read()
    
# zip
import zipfile
with zipfile.ZipFile('data.zip', 'r') as zf:
    file_content = zf.read('my_file.txt')

# In[ ]:


# gzip
import gzip
with gzip.open('data.gz', 'rb') as f:
    file_content = f.read()

# In[ ]:


# bz2
import bz2
with bz2.open('data.bz2', 'rb')
