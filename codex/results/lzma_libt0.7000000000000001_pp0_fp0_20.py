import lzma
lzma.decompress(f)

# lzma.decompress()
# decompress(data, format=FORMAT_AUTO, memlimit=None, filters=None)
# Decompress a LZMA-compressed byte string.
# The data must be formatted according to the LZMA SDK 4.61.
# The parameters format, memlimit and filters have the same meaning as
# in the LZMAFile constructor.
# The data argument must be a byte string. The data object may be reused
# for other decompression calls.

# lzma.FORMAT_AUTO
# Indicate that the format will be automatically detected. This is the
# default format.
# lzma.FORMAT_XZ
# Indicate the .xz file format.
# lzma.FORMAT_ALONE
# Indicate the .lzma file format.
# lzma.FORMAT_RAW
# Indicate raw LZMA streams.
