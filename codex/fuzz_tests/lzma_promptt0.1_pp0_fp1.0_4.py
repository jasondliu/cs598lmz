import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # Test decompression of a simple string
    d = lzma.LZMADecompressor()
    data = d.decompress(b"\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3")
    assert data == b"foo"

    # Test decompression of a string with multiple concatenated
    # compressed streams
    d = lzma.LZMADecompressor()
    data = d.decompress(b"\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3"
                        b"\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x
