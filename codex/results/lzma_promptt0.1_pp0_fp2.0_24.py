import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # Test basic functionality
    d = lzma.LZMADecompressor()
    assert d.unused_data == b""
    assert d.eof is False
    assert d.decompress(b"") == b""
    assert d.unused_data == b""
    assert d.eof is False
    assert d.decompress(b"foo") == b""
    assert d.unused_data == b"foo"
    assert d.eof is False
    assert d.decompress(b"bar") == b""
    assert d.unused_data == b"foobar"
    assert d.eof is False
    assert d.decompress(b"") == b""
    assert d.unused_data == b"foobar"
    assert d.eof is False
    assert d.decompress(b"foo") == b"foobar"
    assert d.unused_data == b""
    assert d.eof is False
    assert d.dec
