from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00')

# lzma.LZMADecompressor.decompress(data, max_length=-1)
# Decompress *data*, returning uncompressed data as bytes.
# If *max_length* is nonnegative, returns at most *max_length* bytes of decompressed data.
# If this limit is reached and further output can be produced, *decompress* will return
# **None**, or raise **LZMAError** if the end of the compressed data stream has been reached.
# In this case, the decompressor object can be used to decompress more data.

# If *max_length* is negative, or if there is no limit on the size of the decompressed data,
# *decompress* will return as much data as possible.

# The decompressor object can be used to decompress data sequentially.
# Decompression objects also have some state which is kept between calls.

# For one-shot decompression, use the decompress() function instead.

