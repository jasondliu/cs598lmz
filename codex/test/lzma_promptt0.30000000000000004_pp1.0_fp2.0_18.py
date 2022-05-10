import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # Test LZMADecompressor
    c = lzma.LZMADecompressor()
    assert c.decompress(b'') == b''
    assert c.unused_data == b''

    assert c.decompress(b'\x00') == b''
    assert c.unused_data == b'\x00'

    assert c.decompress(b'\x00\x00') == b''
    assert c.unused_data == b'\x00\x00'

    assert c.decompress(b'\x00\x00\x00') == b''
    assert c.unused_data == b'\x00\x00\x00'

    assert c.decompress(b'\x00\x00\x00\x00') == b''
    assert c.unused_data == b'\x00\x00\x00\x00'

