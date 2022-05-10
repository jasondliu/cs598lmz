from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# To compress data, we can use a BZ2Compressor object.
from bz2 import BZ2Compressor
compressor = BZ2Compressor()
compressor.compress(data)
compressor.flush()

# The zlib module provides a similar compression facility, as well as the ability to create gzip files directly.
import zlib
data = b'witch which has which witches wrist watch'
len(data)
compressed = zlib.compress(data)
len(compressed)
compressed
decompressed = zlib.decompress(compressed)
decompressed

# The zlib module also contains some convenience functions for working directly with gzip files.
import gzip
s = b'hello world!hello world!hello world!hello world!'
len(s)
t = gzip.compress(s)
len(t)
gzip.decompress(t)

# The gzip module provides a more sophisticated interface for creating and reading gzip files.
import gzip
f = gzip.open('file.txt.
