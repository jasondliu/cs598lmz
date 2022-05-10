from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(data))

# BZ2Compressor
from bz2 import BZ2Compressor
c = BZ2Compressor()
c.compress(data)
c.flush()

# The zlib module provides a lower-level interface to many of the functions in the zlib compression library from GNU.
import zlib
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s)
len(t)
zlib.decompress(t)
zlib.crc32(s)

# The gzip module provides a file-like interface to GNU zip files, using zlib to compress and uncompress the data.
import gzip
f = gzip.open('file.gz', 'wb')
f.write(b'Hello World')
f.close()

import gzip
f = gzip.open('file.gz', 'rb')
f.read()
f.close()

# The lzma module provides support for compressing and decompressing data using the LZMA algorithm
