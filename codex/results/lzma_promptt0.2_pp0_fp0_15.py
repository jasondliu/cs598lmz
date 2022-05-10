import lzma
# Test LZMADecompressor

def test_LZMADecompressor():
    # Test basic functionality
    d = lzma.LZMADecompressor()
    e = lzma.LZMACompressor()
    for i in range(256):
        assert d.decompress(e.compress(bytes([i]))) == bytes([i])
    assert d.decompress(e.flush()) == b""
    assert d.decompress(b"") == b""
    assert d.decompress(b"asdf") == b""
    assert d.unused_data == b"asdf"
    assert d.decompress(b"") == b""
    assert d.unused_data == b""
    # Test multiple concatenated streams
    d = lzma.LZMADecompressor()
    e = lzma.LZMACompressor()
    assert d.decompress(e.compress(b"foo") + e.compress(b"bar") + e.flush()) == b"foobar"
    # Test stream alignment
