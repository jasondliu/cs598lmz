import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # Test basic operation
    d = lzma.LZMADecompressor()
    assert d.eof is False
    assert d.unused_data == b""
    assert d.decompress(b"") == b""
    assert d.unused_data == b""
    assert d.decompress(b"foo") == b"foo"
    assert d.unused_data == b""
    assert d.eof is False
    assert d.decompress(b"") == b""
    assert d.unused_data == b""
    assert d.eof is False
    assert d.decompress(b"bar") == b"bar"
    assert d.unused_data == b""
    assert d.eof is False
    assert d.decompress(b"", max_length=1) == b""
    assert d.unused_data == b""
    assert d.eof is False
