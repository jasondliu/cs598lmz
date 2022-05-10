import lzma
# Test LZMADecompressor

def test_LZMADecompressor_basic():
    c = lzma.LZMADecompressor()
    assert c.decompress(b"") == b""
    assert c.decompress(b"\x00") == b"\x00"
    assert c.decompress(b"\x00" * 100) == b"\x00" * 100
    assert c.decompress(b"\x00" * 100, 100) == b"\x00" * 100
    assert c.decompress(b"\x00" * 100, 10) == b"\x00" * 10
    assert c.decompress(b"\x00" * 100, 0) == b""
    raises(lzma.LZMAError, c.decompress, b"\x00" * 100, 101)
    raises(lzma.LZMAError, c.decompress, b"\x00" * 100, -1)
