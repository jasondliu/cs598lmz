from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# To decompress a file
with open('file.bz2', 'rb') as f:
    data = f.read()
with open('file', 'wb') as f:
    f.write(BZ2Decompressor().decompress(data))

# Compress a file
with open('file', 'rb') as f:
    data = f.read()
with open('file.bz2', 'wb') as f:
    f.write(compress(data))

# Other compression formats
from gzip import compress
from gzip import decompress
from lzma import compress
from lzma import decompress
from zlib import compress
from zlib import decompress

# Decompress a file
with open('file.gz', 'rb') as f:
    data = f.read()
with open('file', 'wb') as f:
    f.write(decompress(data))

with open('file.xz', 'rb') as f:
    data = f.read()
with open('file', '
