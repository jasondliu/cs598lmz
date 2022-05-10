import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # Test that the LZMADecompressor class can decompress a
    # compressed stream.
    data = b"".join(b"test " * 100000)
    cdata = lzma.compress(data)
    d = lzma.LZMADecompressor()
    result = d.decompress(cdata)
    assert result == data
    assert d.unused_data == b""
    assert d.eof

def test_lzma_decompressor_unused_data():
    # Test that the LZMADecompressor class can decompress a
    # compressed stream with extra data at the end.
    data = b"".join(b"test " * 100000)
    cdata = lzma.compress(data)
    cdata += b"extra data"
    d = lzma.LZMADecompressor()
    result = d.decompress(cdata)
    assert result == data
