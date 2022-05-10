from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)
# b'This is the original text.'

# ######################################################################################################################

# Using multiple filters

# A compressor can be constructed using multiple filters.
# The filters are applied in the order in which they are specified.
# For example, the following compressor uses both the LZMA and the BCJ filter:

from lzma import LZMACompressor, FORMAT_XZ, FILTER_LZMA2, FILTER_ARM
compressor = LZMACompressor(format=FORMAT_XZ,
                            check=-1,
                            preset=9,
                            filters=[{'id': FILTER_LZMA2},
                                     {'id': FILTER_ARM, 'preset': 2}])

# ######################################################################################################################

# The format argument specifies the format used to serialize the stream.
# It can be either FORMAT_XZ or FORMAT_ALONE (see the Format documentation).
# The check argument specifies the integrity check used.
# It can be any of the CHECK_* constants,
