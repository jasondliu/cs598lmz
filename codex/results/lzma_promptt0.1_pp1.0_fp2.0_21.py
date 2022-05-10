import lzma
# Test LZMADecompressor.decompress()

def test_decompress():
    # Test decompression of a single-byte string
    d = lzma.LZMADecompressor()
    assert d.decompress(b'\x00') == b''
    assert d.decompress(b'\x01') == b'\x00'
    assert d.decompress(b'\x02') == b'\x01'
    assert d.decompress(b'\x03') == b'\x02'
    assert d.decompress(b'\x04') == b'\x03'
    assert d.decompress(b'\x05') == b'\x04'
    assert d.decompress(b'\x06') == b'\x05'
    assert d.decompress(b'\x07') == b'\x06'
    assert d.decompress(b'\x08') == b'\x07'
    assert d.decompress(b'\x09') == b'\x
