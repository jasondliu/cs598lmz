from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

"""

# The LZMA compression algorithm is designed to be fast and is highly configurable. The algorithm is controlled by an options
# string passed to the LZMACompressor and LZMADecompressor objects.
#
# The options string is a comma-separated list of name=value options. If a name is not specified then the algorithm uses
# its default value.
#
# The following options are supported:
#
# format
#     The format of the compressed data. Currently the only supported value is xz, which is the default.
# check
#     The integrity check used to verify the decompressed data is correct. The default is none. The supported values are:
#
#     crc32
#         CRC-32
#     crc64
#         CRC-64
#     sha256
#         SHA-256
#     none
#         No integrity check is performed.
# filter
#     The filter used by the compressor. If a filter is not specified, the compressor automatically picks one based on the
#     compression level and other options.
#
#     For
