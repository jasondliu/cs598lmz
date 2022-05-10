from lzma import LZMADecompressor
LZMADecompressor().decompress(bytes)

# lzma.LZMADecompressor.decompress(data, max_length=-1)
# Return at most max_length uncompressed bytes, as a bytes object.
# If the data stream has ended and all uncompressed data has been
# processed, this method will return an empty bytes object.
# If the data stream has not yet ended but no more data is available,
# this method will raise an EOFError if max_length is not specified
# (or None) or a ValueError if max_length is negative.
# If the data stream has not yet ended and some data is available,
# this method will return a bytes object containing the available
# uncompressed data, not necessarily of length max_length.

# lzma.LZMADecompressor.unused_data
# The remaining data in the input buffer. This is a bytes object.
# This attribute is not present in the LZMACompressor class.

# lzma.LZMADecompressor.eof
# Whether the data stream has ended, i.e. whether all the
