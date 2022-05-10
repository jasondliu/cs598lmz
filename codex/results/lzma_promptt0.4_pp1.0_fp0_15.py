import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    c = lzma.LZMADecompressor()
    assert c.decompress(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00') == b''
    assert c.decompress(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', max_length=10) == b''
    assert c.decompress(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', max_length=9) == b''
    assert c.decompress(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', max_length=8) == b''
    raises(lzma.LZMAError, c.decompress, b'\x00\x00\x
