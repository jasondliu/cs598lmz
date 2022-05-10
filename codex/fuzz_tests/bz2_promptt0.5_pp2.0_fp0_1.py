import bz2
# Test BZ2Decompressor and BZ2Compressor

def test_BZ2Compressor_decompressor():
    data = b"The quick brown fox jumps over the lazy dog."
    c = bz2.BZ2Compressor()
    d = bz2.BZ2Decompressor()
    data1 = c.compress(data)
    data2 = c.flush()
    data3 = d.decompress(data1)
    data4 = d.decompress(data2)
    assert data == data3 + data4

def test_BZ2Compressor_decompressor_with_eof():
    data = b"The quick brown fox jumps over the lazy dog."
    c = bz2.BZ2Compressor()
    d = bz2.BZ2Decompressor()
    data1 = c.compress(data)
    data2 = c.flush()
    data3 = d.decompress(data1)
    data4 = d.decompress(data2)
    data5 = d.decompress(b"")
    assert
