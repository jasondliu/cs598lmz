import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # Test basic functionality
    d = lzma.LZMADecompressor()
    assert d.decompress(b"") == b""
    assert d.unused_data == b""
    assert d.eof is False
    assert d.decompress(b"asdf") == b"asdf"
    assert d.unused_data == b""
    assert d.eof is False
    assert d.decompress(b"") == b""
    assert d.unused_data == b""
    assert d.eof is False
    assert d.decompress(b"foo") == b"foo"
    assert d.unused_data == b""
    assert d.eof is False
    assert d.decompress(b"", True) == b""
    assert d.unused_data == b""
    assert d.eof is True
    assert d.decompress(b"") == b""
    assert d.unused_data == b""
    assert d
