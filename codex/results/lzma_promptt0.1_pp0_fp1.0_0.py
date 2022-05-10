import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    c = lzma.LZMADecompressor()
    assert c.decompress(b"") == b""
    assert c.unused_data == b""
    assert c.eof is False
    assert c.decompress(b"x") == b""
    assert c.unused_data == b"x"
    assert c.eof is False
    assert c.decompress(b"x") == b""
    assert c.unused_data == b"x"
    assert c.eof is False
    assert c.decompress(b"x", 1) == b""
    assert c.unused_data == b"xx"
    assert c.eof is False
    assert c.decompress(b"x", 1) == b""
    assert c.unused_data == b"xxx"
    assert c.eof is False
    assert c.decompress(b"x", 2) == b""
    assert c.unused_data == b"xxxx
