import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    c = lzma.LZMADecompressor()
    assert not c.eof
    assert c.unused_data == b""
    assert c.decompress(b"") == b""
    assert not c.eof
    assert c.unused_data == b""
    assert c.decompress(b"x") == b""
    assert not c.eof
    assert c.unused_data == b"x"
    assert c.decompress(b"x") == b""
    assert not c.eof
    assert c.unused_data == b"xx"
    assert c.decompress(b"x") == b""
    assert not c.eof
    assert c.unused_data == b"xxx"
    assert c.decompress(b"x") == b""
    assert not c.eof
    assert c.unused_data == b"xxxx"
    assert c.decompress(b"x") == b""
