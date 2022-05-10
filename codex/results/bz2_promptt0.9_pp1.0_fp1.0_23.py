import bz2
# Test BZ2Decompressor compatibility with pyflakes' optional `source` parameter
def test_bz2():
    bz = bz2.BZ2Decompressor()
    bz.decompress(source=None)
