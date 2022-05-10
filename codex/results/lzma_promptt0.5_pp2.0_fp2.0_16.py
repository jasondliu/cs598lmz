import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # Test LZMADecompressor.decompress()
    d = lzma.LZMADecompressor()
    assert d.decompress(b'') == b''
    assert d.decompress(b'\x00') == b''
    assert d.decompress(b'\x00\x00') == b''
    assert d.decompress(b'\x00\x00\x00') == b''
    assert d.decompress(b'\x00\x00\x00\x00') == b''
    assert d.decompress(b'\x00\x00\x00\x00\x00') == b''
    assert d.decompress(b'\x00\x00\x00\x00\x00\x00') == b''
    assert d.decompress(b'\x00\x00\x00\x00\x00\x00\x00') == b''
    assert d.decomp
