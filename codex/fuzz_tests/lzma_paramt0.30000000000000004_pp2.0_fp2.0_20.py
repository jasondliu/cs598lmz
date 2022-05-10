from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# Output: b'hello'

# The LZMA compression algorithm is more efficient than gzip, but it is slower.
# The lzma module has been backported to Python 2. It is also available in the Python 3 standard library as lzma.

# The bz2 module provides a comprehensive interface for the bzip2 compression library. It implements a complete file interface, one shot (de)compression functions, and types for sequential (de)compression.

# The bz2 module provides the following functions:

# bz2.compress(data, compresslevel=9)
# Compress data in one shot. compresslevel can be any integer between 1 and 9.

# bz2.decompress(data)
# Decompress data in one shot.

# bz2.BZ
