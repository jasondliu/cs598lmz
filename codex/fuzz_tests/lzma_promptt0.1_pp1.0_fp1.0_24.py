import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # Test decompression of a single-byte stream
    d = lzma.LZMADecompressor()
    assert d.decompress(b'\x00') == b''
    assert d.decompress(b'\x00' * 100) == b''
    assert d.decompress(b'\x00' * 100, 100) == b''
    assert d.unused_data == b''
    assert d.eof == False
    assert d.decompress(b'\x00') == b''
    assert d.unused_data == b''
    assert d.eof == False
    assert d.decompress(b'\x00', 1) == b''
    assert d.unused_data == b''
    assert d.eof == False
    assert d.decompress(b'\x00', 0) == b''
    assert d.unused_data == b''
    assert d.eof == False
    assert d.decompress(b'
