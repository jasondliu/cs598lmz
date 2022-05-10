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
    assert d.decompress(b"x") == b""
    assert d.unused_data == b"x"
    assert d.eof is False
    assert d.decompress(b"") == b""
    assert d.unused_data == b"x"
    assert d.eof is False
    assert d.decompress(b"y") == b""
    assert d.unused_data == b"xy"
    assert d.eof is False
    assert d.decompress(b"z") == b""
    assert d.unused_data == b"xyz"
    assert d.eof is False
    assert d.decompress
