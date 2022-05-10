import lzma
# Test LZMADecompressor

def test_lzmadecompressor():
    c = lzma.LZMADecompressor()
    data = b"foo"
    assert c.decompress(data) == b"foo"
    assert c.decompress(b"") == b""
    assert c.decompress(b"", max_length=1) == b""

    # Test that LZMADecompressor.decompress() doesn't crash
    # when decompressed data contains embedded zeros.
    # Issue #16222.
    c = lzma.LZMADecompressor()
    assert c.decompress(b"\x00\x00\x00\x00\x00\x00\x00") == b"\0" * 7
    assert c.decompress(b"\x00\x00\x00\x00\x00\x00\x00", max_length=1) == b"\0"
