import lzma
# Test LZMADecompressor

def test_LZMADecompressor():
    c = lzma.LZMADecompressor()
    assert c.decompress(b'Y') == b''
    assert c.decompress(b'X') == b'foo'
    assert c.decompress(b'Y') == b''
    assert c.decompress(b'X') == b'bar'
    assert c.decompress(b'Y') == b''
    assert c.decompress(b'X') == b'baz'
    assert c.decompress(b'Y') == b''
    assert c.decompress(b'X') == b'qux'
    assert c.decompress(b'Y') == b''
    assert c.decompress(b'X') == b'quux'
    assert c.decompress(b'Y') == b''
    assert c.decompress(b'X') == b'corge'
    assert c.decompress(b'Y') == b''
    assert
