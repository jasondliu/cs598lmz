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
    assert c.decompress(b'garbage') == b''
    assert c.unused_data == b'garbagegarbage'
    assert c.eof == False
    assert c.decompress(b'garbage', 1) == b''
    assert c.unused_data == b'arbagegarbage'
    assert c.eof == False
    assert c.decompress(b'garbage', 2) == b'g'
    assert c.unused_data == b'arbagegarbage'
    assert c.eof == False
