import lzma
# Test LZMADecompressor.

def test_decompressor():
    c = lzma.LZMADecompressor()
    assert c.eof is False
    assert c.unused_data == b""

    # Decompress the empty string
    assert c.decompress(b"") == b""
    assert c.eof is False
    assert c.unused_data == b""

    # Decompress the empty string again
    assert c.decompress(b"") == b""
    assert c.eof is False
    assert c.unused_data == b""

    # Decompress a short string
    assert c.decompress(b"x") == b""
    assert c.eof is False
    assert c.unused_data == b"x"

    # Decompress a short string again
    assert c.decompress(b"x") == b""
    assert c.eof is False
    assert c.unused_data == b"xx"

    # Decompress a short string again
    assert c.decompress(b"
