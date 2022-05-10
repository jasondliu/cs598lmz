import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    c = lzma.LZMADecompressor()
    data = c.decompress(b'\x00')
    assert data == b''
    data = c.decompress(b'\x00' * 100)
    assert data == b''
    data = c.decompress(b'\x00' * 100, 100)
    assert data == b''
    data = c.decompress(b'\x00' * 100, 10)
    assert data == b''
    data = c.decompress(b'\x00' * 100, 10)
    assert data == b''
    raises(EOFError, c.decompress, b'')
    raises(EOFError, c.decompress, b'', 100)
    raises(ValueError, c.decompress, b'\x00' * 100, sys.maxsize + 1)
    raises(ValueError, c.decompress, b'\x00' * 100, -1)
    raises(
