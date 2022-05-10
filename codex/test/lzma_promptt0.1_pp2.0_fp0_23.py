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
    assert d.decompress(b"x") == b""
    assert d.eof is False
    assert d.unused_data == b"x"
    assert d.decompress(b"y") == b""
    assert d.eof is False
    assert d.unused_data == b"xy"
    assert d.decompress(b"z") == b""
    assert d.eof is False
    assert d.unused_data == b"xyz"
    assert d.decompress(b"a") == b"a"
    assert d.eof is False
    assert d.unused_data == b"z"
