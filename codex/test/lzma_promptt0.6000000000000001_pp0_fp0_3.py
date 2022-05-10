import lzma
# Test LZMADecompressor

def test_lzma_decompressor_simple():
    d = lzma.LZMADecompressor()
    assert d.decompress(b'\x00') == b''
    assert d.decompress(b'\x00\x00') == b''
    assert d.decompress(b'\x00\x00\x00') == b''
    assert d.decompress(b'\x00\x00\x00\x00') == b''
    assert d.decompress(b'\x00\x00\x00\x00\x00') == b''
    assert d.decompress(b'\x00\x00\x00\x00\x00\x00') == b''
    assert d.decompress(b'\x00\x01\x00\x00\x00\x00\x00\x00') == b'\x00'
