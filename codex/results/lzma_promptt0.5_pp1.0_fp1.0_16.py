import lzma
# Test LZMADecompressor
def test_LZMADecompressor():
    # Test basic functionality
    c = lzma.LZMADecompressor()
    assert c.decompress(b'') == b''
    assert c.unused_data == b''
    assert c.eof == False
    c.decompress(b'garbage')
    assert c.unused_data == b'garbage'
    assert c.eof == False
    # Test multiple decompress() calls
    c = lzma.LZMADecompressor()
    d = c.decompress(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                     b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                     b'\x00\x00\x00\x00\x00\x00
