import lzma
lzma.decompress(compressed_data)

# Output: b'The quick brown fox jumps over the lazy dog.'

# The LZMA module also provides a built-in compressor using the LZMA algorithm.
# It works like the zlib.compress() function, but the compression level parameter
# must be an integer between 0 and 9.


import lzma
data = b'The quick brown fox jumps over the lazy dog.'
compressed = lzma.compress(data, preset=9)
compressed

# Output: b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x00\x00\x00\x00\x00\x00\x00\x00'

# The lzma.compress() function returns a bytes object containing the compressed data.
# Use the lzma.decompress() function to restore the original data.

import
