import lzma
# Test LZMADecompressor

def test_LZMADecompressor():
    c = lzma.LZMADecompressor()
    assert c.eof is False
    assert c.unused_data == b""
    assert c.decompress(b"") == b""
    assert c.eof is False
    assert c.unused_data == b""
    assert c.decompress(b"\x00") == b""
    assert c.eof is False
    assert c.unused_data == b""
    assert c.decompress(b"\x00\x00") == b""
    assert c.eof is False
    assert c.unused_data == b""
    assert c.decompress(b"\x00\x00\x00") == b""
    assert c.eof is False
    assert c.unused_data == b""
    assert c.decompress(b"\x00\x00\x00\x00") == b""
    assert c.eof is False
    assert c.unused_
