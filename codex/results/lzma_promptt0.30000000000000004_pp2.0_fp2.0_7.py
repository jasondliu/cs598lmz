import lzma
# Test LZMADecompressor

def test_LZMADecompressor():
    c = lzma.LZMADecompressor()
    assert c.decompress(b'') == b''
    assert c.unused_data == b''
    assert c.eof == False
    c.decompress(b'garbage')
    assert c.unused_data == b'garbage'
    assert c.eof == False
    c.decompress(b'garbage', 2)
    assert c.unused_data == b'bage'
    assert c.eof == False
    c.decompress(b'garbage', 2)
    assert c.unused_data == b'ge'
    assert c.eof == False
    c.decompress(b'garbage', 2)
    assert c.unused_data == b''
    assert c.eof == False
    c.decompress(b'garbage', 2)
    assert c.unused_data == b''
    assert c.eof == False
    c.decomp
