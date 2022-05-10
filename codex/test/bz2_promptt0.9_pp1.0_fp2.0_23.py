import bz2
# Test BZ2Decompressor
data = b'If compressed data is detected, autodetect its type and decompress it.'
compressor = bz2.BZ2Decompressor()
