import lzma
# Test LZMADecompressor

def test_LZMADecompressor():
    assert lzma.LZMADecompressor().eof == False
    assert lzma.LZMADecompressor().unused_data == b''
    assert lzma.LZMADecompressor().decompress(b'\x00') == b''
    assert lzma.LZMADecompressor().eof == True
    assert lzma.LZMADecompressor().unused_data == b''
    assert lzma.LZMADecompressor().decompress(b'\x00') == b''
    assert lzma.LZMADecompressor().eof == True
    assert lzma.LZMADecompressor().unused_data == b''
    assert lzma.LZMADecompressor().decompress(b'\x00', max_length=1) == b''
    assert lzma.LZMADecompressor().eof == True
    assert lzma.LZMAD
