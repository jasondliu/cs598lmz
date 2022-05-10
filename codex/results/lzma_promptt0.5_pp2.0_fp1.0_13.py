import lzma
# Test LZMADecompressor.decompress() and LZMADecompressor.eof

def test_decompress_eof():
    if not hasattr(lzma, 'LZMADecompressor'):
        pytest.skip('requires lzma module')

    c = lzma.LZMADecompressor()
    data = b'1234567890'
    assert c.decompress(data) == data
    assert not c.eof
    assert c.decompress(b'') == b''
    assert c.eof
    assert c.decompress(data) == b''
    assert c.eof

def test_decompress_non_bytes():
    if not hasattr(lzma, 'LZMADecompressor'):
        pytest.skip('requires lzma module')

    c = lzma.LZMADecompressor()
    with pytest.raises(TypeError):
        c.decompress(bytearray(b'1234567890'))

def test_decomp
