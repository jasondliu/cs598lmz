from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# In[]:
# lz4
import lz4.frame
import lz4
lz4.frame.decompress(data)
lz4.decompress(data)

# In[]:
# gzip
import gzip
gzip.decompress(data)

# In[]:
# brotli
import brotli
brotli.decompress(data)

# In[]:
# zstd
import zstd
zstd.ZstdDecompressor(None, {'dict': dict_data}).decompress(data)

# In[]:
# lzma
import lzma
lzma.decompress(data)

# In[]:
# zlib
import zlib
zlib.decompress(data)

# In[]:
# zopfli
import zopfli.zlib
zopfli.zlib.decompress(data)

# In[]:
# miss_hannigan.decompressors
import miss_h
