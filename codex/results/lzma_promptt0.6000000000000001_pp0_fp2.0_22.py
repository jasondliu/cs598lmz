import lzma
# Test LZMADecompressor.decompress()

def test_decompress():
    c = lzma.LZMADecompressor()
    assert c.decompress(b"foo") == b"foo"
    assert c.decompress(b"foo") == b""

    # Unused data after the end of a stream should be ignored
    assert c.decompress(b"bar") == b"bar"

    # Test multiple concatenated streams
    c = lzma.LZMADecompressor()
    assert c.decompress(b"foo") == b"foo"
    assert c.decompress(b"bar") == b"bar"
    assert c.decompress(b"baz") == b"baz"
    assert c.decompress(b"quux") == b"quux"

    # Decompressing empty string should return empty string
    c = lzma.LZMADecompressor()
    assert c.decompress(b"") == b""

    # Check that random data raises an exception (except on Python 3
