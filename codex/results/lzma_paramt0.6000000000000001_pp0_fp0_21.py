from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

data = open('../data/train.csv.bz2', 'rb').read()

bz2.decompress(data)

data = open('../data/train.csv.xz', 'rb').read()

lzma.decompress(data)

# you can also use xz-utils to extract .xz files
# import subprocess
# subprocess.run(['xz', '-d', '../data/train.csv.xz'])


# # Compression and decompression with gzip
# 
# - `gzip.open(filename, mode)`
#     - `mode` can be `'r'`, `'rb'`, `'w'`, `'wb'`, `'a'`, `'ab'`

# In[5]:


import gzip

with gzip.open('../data/train.csv.gz', 'rb') as f:
    file_content = f.read()
    
print(file_content[:10])


# # Compression and decomp
