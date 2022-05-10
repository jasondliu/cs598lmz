import bz2
bz2.decompress(data)

# If you need to decompress a file in memory, however, you can use a BytesIO object as a wrapper for the compressed data:

# In[4]:

from io import BytesIO

compressed_file = BytesIO(data)
decompressor = bz2.BZ2Decompressor()

final_data = decompressor.decompress(compressed_file.read())
final_data

# ## Using lzma for XZ Compression

# In[5]:

import lzma

with lzma.open('lzma_compressed.xz', 'wt') as f:
    f.write(text)

with lzma.open('lzma_compressed.xz') as f:
    print(f.read())

# In[6]:

data = lzma.compress(b'This is some data')
data

# In[7]:

lzma.decompress(data)

# ## Using zlib for zlib and gzip
