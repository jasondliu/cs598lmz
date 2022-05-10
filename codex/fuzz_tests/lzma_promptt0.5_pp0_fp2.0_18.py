import lzma
# Test LZMADecompressor

def test_LZMADecompressor_simple():
    # Test basic functionality.
    comp = lzma.LZMADecompressor()
    assert not comp.eof
    assert comp.unused_data == b""
    assert comp.decompress(b"") == b""
    assert comp.unused_data == b""
    assert comp.decompress(b"x") == b""
    assert comp.unused_data == b"x"
    assert comp.decompress(b"") == b""
    assert comp.unused_data == b"x"
    assert comp.decompress(b"y") == b""
    assert comp.unused_data == b"xy"
    assert comp.decompress(b"abcdef") == b""
    assert comp.unused_data == b"xyabcdef"
    assert comp.decompress(b"") == b""
    assert comp.unused_data == b"xyabcdef"
    assert comp.decompress(b"123456") == b""

