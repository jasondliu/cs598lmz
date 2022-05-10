from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# To compress data, use the LZMACompressor class:

from lzma import LZMACompressor
compressor = LZMACompressor()
compressor.compress(data)
compressor.flush()

# By default, the LZMACompressor class uses the FILTER_LZMA2 filter,
# which is a good general purpose filter for XZ data.
# If you want to use the older LZMA filter instead,
# pass FILTER_LZMA as the filter_name parameter to the constructor.
# The LZMA filter is faster to compress to and decompress from,
# but the LZMA2 filter produces smaller compressed data.

# The LZMACompressor class supports the same filters
# as the LZMADecompressor class.
# However, only the FILTER_LZMA2 filter is supported
# when compressing data to the .xz file format.

# When you are done compressing data, you should call the flush() method
# to make sure that all pending data has been processed.
# This is necessary
