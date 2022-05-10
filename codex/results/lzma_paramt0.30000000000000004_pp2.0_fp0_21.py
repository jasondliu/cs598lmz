from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# In[ ]:


# 压缩
from lzma import LZMACompressor
compressor = LZMACompressor()
compressor.compress(b"some data")
compressor.flush()

# In[ ]:


# 压缩
from bz2 import BZ2Compressor
compressor = BZ2Compressor()
compressor.compress(b"some data")
compressor.flush()

# In[ ]:


# 解压
from bz2 import BZ2Decompressor
decompressor = BZ2Decompressor()
decompressor.decompress(data)

# In[ ]:


# 压缩
import zlib
compressor = zlib.compressobj()
compressor.compress(b"some data")
compressor.flush()

# In[ ]:


# 解压
import zlib
decompressor = zlib.decompressobj()
decompressor.decompress(data)
