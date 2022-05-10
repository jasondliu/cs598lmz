import lzma
# Test LZMADecompressor.read()

def test(data):
    c = lzma.LZMADecompressor()
    d = c.decompress(data)
    assert c.unused_data == b''
    assert c.eof is True
    assert c.decompress(b'x') == b''
    assert c.unused_data == b'x'
    assert c.eof is False
    assert c.decompress(b'') == b''
    assert c.unused_data == b'x'
    assert c.eof is False
    assert c.decompress(b'y') == b''
    assert c.unused_data == b'xy'
    assert c.eof is False
    assert c.decompress(b'z') == b''
    assert c.unused_data == b'xyz'
    assert c.eof is False
    assert c.decompress(b'x') == b''
    assert c.unused_data == b'xyzx'
    assert c.eof is False

