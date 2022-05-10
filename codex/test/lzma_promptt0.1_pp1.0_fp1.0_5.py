import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00'
    d = lzma.LZMADecompressor()
    assert d.decompress(data) == b'12345abcde'
    assert d.unused_data == b''
    assert d.eof is True
    raises(EOFError, d.decompress, b'')
    raises(ValueError, d.decompress, b'\xff')
    raises(ValueError, d.decompress, b'\xff' * 5)
    raises(ValueError, d.decompress, b'\xff' * 5 + b'\x00' * 2)
