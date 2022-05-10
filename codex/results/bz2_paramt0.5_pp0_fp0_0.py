from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# In[ ]:

import zlib
zlib.decompress(data, -zlib.MAX_WBITS)


# In[ ]:

import lzma
lzma.decompress(data)


# In[ ]:

import lzma
lzma.decompress(data)


# In[ ]:

import brotli
brotli.decompress(data)


# In[ ]:

import gzip
gzip.decompress(data)


# In[ ]:

import lz4.frame
lz4.frame.decompress(data)


# In[ ]:

import lzma
lzma.decompress(data)


# In[ ]:

import lzma
lzma.decompress(data)


# In[ ]:

import lzma
lzma.decompress(data)


# In[ ]:

import lzma
lzma.decompress(data
