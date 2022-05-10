import bz2
# Test BZ2Decompressor.decompress()

for size in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    data = b'x' * size
    assert bz2.decompress(bz2.compress(data)) == data
    assert bz2.BZ2Decompressor().decompress(bz2.compress(data)) == data
# Test BZ2Decompressor.decompress() with multiple calls

for size in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    data = b'x' * size
    d = bz2.BZ2Decompressor()
