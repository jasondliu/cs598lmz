import bz2
# Test BZ2Decompressor with a file containing an empty stream.

data = bz2.BZ2Compressor().compress(b'')
assert bz2.decompress(data) == b''

