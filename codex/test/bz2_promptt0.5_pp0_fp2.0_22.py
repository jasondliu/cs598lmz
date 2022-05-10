import bz2
# Test BZ2Decompressor.decompress()

def test_BZ2Decompressor_decompress():
    # Test decompression of empty string
    d = bz2.BZ2Decompressor()
    assert d.decompress(b'') == b''
    assert d.decompress(b'\x00\x00\x00\x00\x00\x00\x00\x00BZh0') == b''
    # Test decompression of empty string with unconsumed data
    d = bz2.BZ2Decompressor()
    assert d.decompress(b'\x00\x00\x00\x00\x00\x00\x00\x00BZh0\x00\x00\x00\x01\x00\x00\x00\x01') == b''
    # Test decompression of short string
    d = bz2.BZ2Decompressor()
