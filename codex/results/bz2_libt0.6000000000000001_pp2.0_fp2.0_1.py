import bz2
bz2.decompress(bz2_data)
 
# bz2.BZ2File is a lower-level class for working with bz2 files
file_data = bz2.BZ2File('./test_data/bz2_test.bz2').read()
file_data


# In[ ]:


#Gzip compression
import gzip
gzip.open('./test_data/gz_test.gz', 'rt').read()


# In[ ]:


#LZMA compression
import lzma
with lzma.open('./test_data/lzma_test.xz', 'rt') as f:
    file_data = f.read()
file_data


# In[ ]:


#zipfile module
from zipfile import ZipFile

with ZipFile('./test_data/zip_test.zip', 'r') as zf:
    print(zf.namelist())
    zf.extractall('./test_data/extract')
    with zf.open('
