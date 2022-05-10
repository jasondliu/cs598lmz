import bz2
# Test BZ2Decompressor.decompress() with bz2.decompress()
def decompress(data):
    res = []
    d = decompressobj()
    res.append(d.decompress(data))
    res.append(d.flush())
    return b"".join(res)
def test_decompress(s, limit=None):
    test_s = s[:limit]
    d = decompress(s)
    d2 = bz2.decompress(test_s)
    assert d == d2, (d, d2)
def test_decompress_whole():
    test_s = bz2.compress(b"foo")
    test_decompress(test_s)
def test_decompress_chunked():
    test_s = bz2.compress(b"foo")
    test_decompress(test_s, limit=1)
    test_decompress(test_s, limit=2)
    test_decompress(test_s, limit=3)
