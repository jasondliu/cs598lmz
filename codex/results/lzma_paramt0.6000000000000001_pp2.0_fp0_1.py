from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

# The lzma module supports compressing and decompressing data streams with
# the LZMA, XZ, and legacy LZMA compression algorithms.

# The LZMAFile class implements a file-like object that reads and writes
# data transparently compressed or decompressed with the LZMA algorithm.
# It takes a file-like object as the first argument, and optionally a
# format, mode, and filters keyword arguments.
# The format keyword argument specifies the format of the stream, and
# must be either 'xz' or 'lzma' (the default).
# The mode keyword argument specifies the mode of the stream, and must be
# one of 'r' (the default) for reading, or 'w' for writing.
# The filters keyword argument specifies a list of filters to use when
# decompressing.
# The filters argument must be a list of dicts with a 'id' key and a
# 'dict_size' key.
# The 'id' key specifies the filter ID and must be one of 'lzma2' (the
# default) or '
