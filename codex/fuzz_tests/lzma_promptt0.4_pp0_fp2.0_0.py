import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    c = lzma.LZMADecompressor()
    assert c.decompress(b'') == b''
    assert c.unused_data == b''
    assert c.eof
    assert c.decompress(b'x') == b''
    assert c.unused_data == b'x'
    assert c.eof
    assert c.decompress(b'y', 2) == b''
    assert c.unused_data == b'xy'
    assert c.eof
    assert c.decompress(b'\x00\x00\x00\x00\x00\x00\x00\x00'
                          b'\x00\x00\x00\x00\x00\x00\x00\x00'
                          b'\x00\x00\x00\x00\x00\x00\x00\x00'
                          b'\x00\x00\x00\x00\x00\
