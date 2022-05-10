import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # Test decompression using the decompressor object
    cdata = lzma.compress(b"this is a test")
    d = lzma.LZMADecompressor()
    data = d.decompress(cdata)
    assert data == b"this is a test"
    assert d.unused_data == b""
    assert d.eof is True
    # Test decompression using the decompress() convenience function
    data = lzma.decompress(cdata)
    assert data == b"this is a test"
    # Test partial decompression
    d = lzma.LZMADecompressor()
    data = d.decompress(cdata[:4])
    assert data == b""
    assert d.unused_data == cdata[:4]
    assert d.eof is False
    data = d.decompress(cdata[4:])
    assert data == b"this is a test"
    assert d.unused_data == b""
