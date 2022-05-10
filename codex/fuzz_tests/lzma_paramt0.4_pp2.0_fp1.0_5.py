from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_RAW, memlimit=None, filters=None)

# lzma.LZMADecompressor.decompress(data, max_length=None)
# LZMADecompressor.decompress(data, max_length=None)
# Decompress data, returning uncompressed data as bytes.
# If the data is not a valid LZMA-compressed data, a FormatError is raised.
# If max_length is not None, the return value will be no longer than max_length.
# Unconsumed input data will be stored in the unused_data attribute.
# If the input is compressed with the LZMA_CONCATENATED format,
# the data will be decompressed in chunks, and the return value
# will be a generator yielding the decompressed chunks.

# lzma.LZMADecompressor.flush()
# LZMADecompressor.flush()
# Flush the decompressor object and return the remaining unconsumed input data,
# if any.

# lzma.LZMADecompressor.copy
