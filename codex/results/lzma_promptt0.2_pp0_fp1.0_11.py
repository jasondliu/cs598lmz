import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # Test decompression of a simple string
    d = lzma.LZMADecompressor()
    data = d.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6B\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x00\x00\x04\x00\x00\x00\x00')
    assert data == b'12345abcde'

    # Test decompression of a longer string
    d = lzma.LZMADecompressor()
    data = d.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6B\x02\x00!\x01\x1a\x00\x00\x00t/\xe5\xa3\x01\x00\x00\x04\x00\x00\x00\x
