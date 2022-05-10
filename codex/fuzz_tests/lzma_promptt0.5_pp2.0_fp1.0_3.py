import lzma
# Test LZMADecompressor

def test_lzma_decompressor_type():
    assert lzma.LZMADecompressor().__class__ is lzma.LZMADecompressor

def test_lzma_decompressor_decompress():
    data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x00\x00\xc0'
    decomp = lzma.LZMADecompressor()
    assert decomp.decompress(data) == b'12345abcde'
    assert decomp.unused_data == b''
    raises(IOError, decomp.decompress, b'')

def test_lzma_decompressor_flush():
    data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x
