import lzma
# Test LZMADecompressor

def test_decompressor():
    c = lzma.LZMADecompressor()
    assert c.decompress(b"") == b""
    assert c.unused_data == b""
    assert c.eof is False
    assert c.decompress(b"x") == b"x"
    assert c.unused_data == b""
    assert c.eof is False
    assert c.decompress(b"x" * 100) == b"x" * 100
    assert c.unused_data == b""
    assert c.eof is False
    assert c.decompress(b"", True) == b""
    assert c.unused_data == b""
    assert c.eof is True
    assert c.decompress(b"x") == b""
    assert c.unused_data == b"x"
    assert c.eof is True
    assert c.decompress(b"x" * 100) == b""
    assert c.unused_data == b"x" * 100
