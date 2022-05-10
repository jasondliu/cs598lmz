import bz2
# Test BZ2Decompressor.read with a large buffer size
# to make sure it doesn't return a short buffer
d = bz2.BZ2Decompressor()
result = d.read(1024)
assert len(result) == 1024
# Test BZ2Decompressor.decompress with a large buffer size
# to make sure it doesn't return a short buffer
d = bz2.BZ2Decompressor()
result = d.decompress(d.decompress(COMPRESSED))
assert len(result) == 1024
