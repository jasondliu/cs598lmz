import bz2
# Test BZ2Decompressor.decompress with a data that is larger than the internal
# buffer.

data = bz2.BZ2Decompressor().decompress(bz2.compress(b"foo"))
print(data)
