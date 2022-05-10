import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    c = lzma.LZMADecompressor()
    assert c.decompress(b'') == b''
    assert c.unused_data == b''
    assert c.eof is False

    c = lzma.LZMADecompressor()
    assert c.decompress(b'\x00') == b''
    assert c.unused_data == b'\x00'
    assert c.eof is False

    c = lzma.LZMADecompressor()
    assert c.decompress(b'\x00\x00') == b''
    assert c.unused_data == b'\x00\x00'
    assert c.eof is False

    c = lzma.LZMADecompressor()
    assert c.decompress(b'\x00\x00\x00') == b''
    assert c.unused_data == b'\x00\x00\x00'
    assert c.
