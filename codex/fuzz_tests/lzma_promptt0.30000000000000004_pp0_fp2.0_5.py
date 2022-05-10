import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # Test decompressor with various input sizes
    c = lzma.LZMADecompressor()
    for i in range(256):
        data = b'X' * i
        assert c.decompress(data) == data
        assert c.unused_data == b''
        assert c.eof is False
    assert c.decompress(b'', True) == b''
    assert c.unused_data == b''
    assert c.eof is True
    assert c.decompress(b'X') == b''
    assert c.unused_data == b'X'
    assert c.eof is True
    # Test decompressor object with various input sizes
    c = lzma.LZMADecompressor()
    for i in range(1, 257):
        data = b'X' * i
        assert c.decompress(data) == data
        assert c.unused_data == b''
        assert c.eof is False
    assert c.
