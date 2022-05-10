import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # Test decompressor with a small input
    c = lzma.LZMADecompressor()
    data = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    assert c.decompress(data) == b''
    assert c.unused_data == b''
    assert c.eof is False
    assert c.needs_input is True
    assert c.needs_input is True
    assert c.decompress(b'', max_length=1) == b''
    assert c.unused_data == b''
    assert c.eof is False
    assert c.needs_input is True
    assert c.needs_input is True
    assert c.decompress(b'', max_length=0) == b''
    assert c.unused_data == b''
    assert c.eof is False
