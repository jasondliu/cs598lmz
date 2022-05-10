import lzma
# Test LZMADecompressor.decompress()

def test_decompress():
    c = lzma.LZMADecompressor()
    assert c.decompress(b'') == b''
    assert c.decompress(b'\x00') == b''
    assert c.decompress(b'\x00\x00') == b''
    assert c.decompress(b'\x00\x00\x00') == b''
    assert c.decompress(b'\x00\x00\x00\x00') == b''
    assert c.decompress(b'\x00\x00\x00\x00\x00') == b''
    assert c.decompress(b'\x00\x00\x00\x00\x00\x00') == b''
    assert c.decompress(b'\x00\x00\x00\x00\x00\x00\x00') == b''
    assert c.decompress(b'\x00\x00\x00\x
