import lzma
# Test LZMADecompressor

def test_lzma_decompressor_simple():
    data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x00\x00\x04\x00\x00\x00\x00'
    d = lzma.LZMADecompressor()
    assert d.decompress(data) == b'12345abcde'
    assert d.unused_data == b''
    d = lzma.LZMADecompressor()
    assert d.decompress(data[:1]) == b''
    assert d.unused_data == data[:1]
    assert d.decompress(data[1:]) == b'12345abcde'
    assert d.unused_data == b''
    d = lzma.LZMADecompressor()
    assert d.decompress(
