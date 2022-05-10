import lzma
# Test LZMADecompressor

def test_LZMADecompressor():
    c = lzma.LZMADecompressor()
    assert c.decompress(b'') == b''
    assert c.decompress(b'x') == b'x'
    assert c.decompress(b'y') == b'y'
    assert c.decompress(b'z') == b'z'
    c = lzma.LZMADecompressor()
    assert c.decompress(b'\xc0') == b''
    assert c.decompress(b'x') == b'x'
    assert c.decompress(b'y') == b'y'
    assert c.decompress(b'z') == b'z'
    c = lzma.LZMADecompressor()
    assert c.decompress(b'\xc0xy') == b'xy'
    assert c.decompress(b'z') == b'z'
    c = lzma.LZMADecompressor
