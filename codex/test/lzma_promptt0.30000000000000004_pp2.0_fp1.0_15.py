import lzma
# Test LZMADecompressor

# Test decompressor
def test_decompressor():
    c = lzma.LZMADecompressor()
    assert c.decompress(b'') == b''
    assert c.flush() == b''
    assert c.decompress(b'\x00') == b''
    assert c.flush() == b''
    assert c.decompress(b'\x00\x00') == b''
    assert c.flush() == b''
    assert c.decompress(b'\x00\x00\x00') == b''
    assert c.flush() == b''
    assert c.decompress(b'\x00\x00\x00\x00') == b''
    assert c.flush() == b''
    assert c.decompress(b'\x00\x00\x00\x00\x00') == b''
    assert c.flush() == b''
