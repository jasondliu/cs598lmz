import lzma
# Test LZMADecompressor
def test_LZMADecompressor():
    c = lzma.LZMADecompressor()
    assert c.decompress(b"") == b""
    assert c.decompress(b"123") == b"123"
    assert c.decompress(b"112233") == b"123"
    py.test.raises(lzma.LZMAError, c.decompress, b"\x00")
    py.test.raises(lzma.LZMAError, c.decompress, b"\x00"*5)
    py.test.raises(lzma.LZMAError, c.decompress, b"\x00"*5 + b"123")
    d = lzma.LZMADecompressor()
    assert d.decompress(b"\x00"*4 + b"123") == b"123"
    assert not d.eof
    assert d.decompress(b"") == b""
    assert d.eof
