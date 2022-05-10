import lzma
# Test LZMADecompressor

# Test LZMADecompressor

def test_LZMADecompressor():
    # Test basic functionality
    c = lzma.LZMADecompressor()
    assert c.decompress(b'X') == b'X'
    assert c.decompress(b'Y') == b'Y'
    assert c.decompress(b'Z') == b'Z'
    assert c.decompress(b'') == b''
    assert c.decompress(b'a') == b'a'
    assert c.decompress(b'b') == b'b'
    assert c.decompress(b'c') == b'c'
    assert c.unused_data == b''
    raises(lzma.LZMAError, c.decompress, b'\x00')
    assert c.unused_data == b'\x00'

    # Test multiple decompress() calls
    c = lzma.LZMADecompressor()
    assert c.decompress(
