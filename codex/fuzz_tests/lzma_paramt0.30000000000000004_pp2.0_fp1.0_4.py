from lzma import LZMADecompressor
LZMADecompressor.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')

# decompress
# decompress(data, max_length=-1, format=FORMAT_AUTO, memlimit=None, filters=None)
#
# Decompress data (a bytes object), returning the uncompressed data as a bytes object.
#
# If max_length is nonnegative, returns at most max_length bytes of decompressed data.
# If this limit is reached and further output can be produced,
# the decompressor will return an exception.
#
# If format is FORMAT_AUTO (the default), the decompressor will automatically detect the
# format of the input data.
#
# If format is FORMAT_XZ, the input data must be in the XZ Container format.
#
# If format is FORMAT_ALONE, the input data must be in the raw (single-
