import lzma
lzma.decompress(open('/tmp/lzma', 'rb').read())

# In[ ]:

import zlib
zlib.decompress(open('/tmp/zlib', 'rb').read())

# In[ ]:

import bz2
bz2.BZ2Decompressor().decompress(open('/tmp/bz2', 'rb').read())

# In[ ]:

import snappy
snappy.decompress(open('/tmp/snappy', 'rb').read())

# In[ ]:

import lz4.block
lz4.block.decompress(open('/tmp/lz4', 'rb').read())

# In[ ]:

import lz4.frame
lz4.frame.decompress(open('/tmp/lz4frame', 'rb').read())

# In[ ]:

import xxhash, xxhash.xxh64
h = xxhash.xxh64()
h.update(open('/tmp/zlib', 'rb').
