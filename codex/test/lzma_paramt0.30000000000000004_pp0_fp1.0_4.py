from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# Output: b'hello'

# The LZMA file format is described in the lzma documentation.
# The lzma module does not support compression, but it does support decompression.
# The format is a simple wrapper around LZMA2 streams.
# The LZMA2 format is described in the XZ Utils documentation.
# The format is also used in the xz command line tool.
# The lzma module does not support compression, but it does support decompression.
# The format is a simple wrapper around LZMA2 streams.
# The LZMA2 format is described in the XZ Utils documentation.
# The format is also used in the xz command line tool.
# The lzma module does not support compression, but it does support decompression.
# The format is a simple wrapper
