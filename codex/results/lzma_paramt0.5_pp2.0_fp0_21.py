from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# lzma.LZMADecompressor.decompress(data, max_length=None)
# Decompress *data*, returning uncompressed data as bytes.
# If *max_length* is nonnegative, returns at most *max_length* bytes of
# decompressed data. If this limit is exceeded and if *decompress* is called
# again, the first call will complete without returning any data.
# This limit is applied separately for the initial call and for all subsequent
# calls: *max_length* is the total of decompressed data returned in all calls
# so far, not the maximum amount of data to be returned in a single call.
# Raises EOFError if the end of the compressed data stream is reached before
# the entire uncompressed data stream has been read.
# Raises lzma.LZMAError if any of the input data was corrupted.
# Raises ValueError if max_length is exceeded.
# Raises OSError if the input data was truncated or corrupted.

# lzma.LZMADecompressor.
