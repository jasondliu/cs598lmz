import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # Test basic functionality
    d = lzma.LZMADecompressor()
    assert d.eof is False
    assert d.unused_data == b""
    assert d.decompress(b"") == b""
    assert d.eof is False
    assert d.unused_data == b""
    assert d.decompress(b"foo") == b""
    assert d.eof is False
    assert d.unused_data == b"foo"
    assert d.decompress(b"bar") == b"foobar"
    assert d.eof is False
    assert d.unused_data == b""
    assert d.decompress(b"") == b""
    assert d.eof is False
    assert d.unused_data == b""
    assert d.decompress(b"") == b""
    assert d.eof is True
    assert d.unused_data == b""
