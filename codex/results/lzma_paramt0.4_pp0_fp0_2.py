from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xf6\xff\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00')

# decompress
# decompress(data, max_length=-1, format=FORMAT_AUTO, memlimit=None, filters=None)
# Decompress data (a bytes object), returning the uncompressed data as a bytes object.
# If the format parameter is given, it is used to determine how to decompress the data.
# If format is omitted or FORMAT_AUTO is given, the decompressor will automatically detect the compressed data format.
# If max_length is nonnegative, it is used as a hard limit of the number of uncompressed bytes returned.
# If the limit is exceeded, LZMAError will be raised.
# If memlimit is non-None, it is used as a hard limit of the amount of memory used by the decompressor.
# If the limit is exceeded, LZMAError will be
