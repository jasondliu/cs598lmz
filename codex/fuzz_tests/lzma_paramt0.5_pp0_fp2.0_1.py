from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# In[ ]:


# lzma
import lzma
lzma.decompress(data)

# In[ ]:


# bz2
import bz2
bz2.decompress(data)

# In[ ]:


# zstandard
import zstandard as zstd
zstd.ZstdDecompressor().decompress(data)

# In[ ]:


# brotli
import brotli
brotli.decompress(data)

# In[ ]:


# blosc
import blosc
blosc.decompress(data)

# In[ ]:


# zlib
import zlib
zlib.decompress(data)

# In[ ]:


# zopfli
import zopfli
zopfli.decompress(data)

# In[ ]:


# zopfli
import zopfli
zopfli.decompress(data)

# In[ ]:


# sn
