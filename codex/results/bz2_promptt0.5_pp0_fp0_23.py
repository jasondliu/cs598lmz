import bz2
# Test BZ2Decompressor with multiple chunks

def test_multiple_chunks():
    data = bz2.compress(b"foo" * 100000)
    c = bz2.BZ2Decompressor()
    d = c.decompress(data[:100])
    d += c.decompress(data[100:1000])
    d += c.decompress(data[1000:])
    assert d == b"foo" * 100000

def test_multiple_chunks_read():
    data = bz2.compress(b"foo" * 100000)
    c = bz2.BZ2Decompressor()
    d = c.decompress(data[:100], 100)
    d += c.decompress(data[100:1000], 900)
    d += c.decompress(data[1000:])
    assert d == b"foo" * 100000

def test_multiple_chunks_read_and_unused_data():
    data = bz2.compress(b"foo" * 100000)
    c = b
