from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# lzma.LZMADecompressor.decompress(data, max_length=None)
# Return at most max_length uncompressed bytes, as a bytes object.
# If this limit is not given, all data is decompressed and returned.
# If the limit is exceeded, LZMAError is raised.
# If the limit is not exceeded, the return value is the concatenation of all
# the decompressed chunks so far.

# lzma.LZMADecompressor.flush()
# Flush the decompressor object and return the remaining decompressed data as
# a bytes object.

# lzma.LZMADecompressor.copy()
# Return a copy of the decompressor object.
# This can be used to decompress data across thread boundaries.

# lzma.LZMADecompressor.eof
# True if the end-of-stream marker has been reached.

# lzma.LZMADecompressor.unused_data
# The portion of the input data which was not consumed by
