import lzma
# Test LZMADecompressor

def test_LZMADecompressor_basic():
    d = lzma.LZMADecompressor()
    data = d.decompress(b'\x00\x00\x00\x00')
    assert data == b''

def test_LZMADecompressor_buffer_size():
    d = lzma.LZMADecompressor()
    data = d.decompress(b'\x00\x00\x00\x00', max_length=2)
    assert data == b''
    data = d.decompress(b'\x00\x00\x00\x00', max_length=2)
    assert data == b''
    data = d.decompress(b'\x00\x00\x00\x00')
    assert data == b''

def test_LZMADecompressor_unused_data():
    d = lzma.LZMADecompressor()
    data = d.decompress(b'\x00\x00
