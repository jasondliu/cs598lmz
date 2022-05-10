from lzma import LZMADecompressor
LZMADecompressor().decompress(bytes(data))

# In[ ]:


# lzma
import lzma

with open("/kaggle/input/avito-demand-prediction/train.csv.zip", 'rb') as f:
    file_content = f.read()

data = lzma.decompress(file_content)
print(data)

# In[ ]:


# gz
import gzip

with gzip.open("/kaggle/input/avito-demand-prediction/train.csv.zip", 'rb') as f:
    file_content = f.read()

data = gzip.decompress(file_content)
print(data)

# In[ ]:


# bz2
import bz2

with bz2.BZ2File("/kaggle/input/avito-demand-prediction/train.csv.zip", 'rb') as f:
    file_content = f.read()

data = bz2.decompress(file_content)
print
