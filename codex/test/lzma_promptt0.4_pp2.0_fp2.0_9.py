import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # Test decompression of a simple string
    c = lzma.LZMADecompressor()
    assert c.decompress(b'XZ\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00\x21\x01\x16\x00\x00\x00\x74\x2f\xe5\xa3\x01\x00\x00\x00\x00') == b'foo'
    assert c.unused_data == b''
    assert c.eof is True

    # Test decompression of a longer string
    c = lzma.LZMADecompressor()
