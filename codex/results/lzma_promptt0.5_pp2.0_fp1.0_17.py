import lzma
# Test LZMADecompressor

@pytest.mark.skipif(not lzma, reason="needs _lzma")
def test_decompressor():
    c = lzma.LZMADecompressor()
    assert c.decompress(b"") == b""
    assert c.unused_data == b""
    assert c.eof is False
    assert c.decompress(b"foo") == b""
    assert c.unused_data == b"foo"
    assert c.eof is False
    assert c.decompress(b"bar") == b""
    assert c.unused_data == b"foobar"
    assert c.eof is False
    assert c.decompress(b"") == b""
    assert c.unused_data == b"foobar"
    assert c.eof is False
    assert c.decompress(b"foo") == b"foobar"
    assert c.unused_data == b""
    assert c.eof is False
    assert c.decompress(b"") == b
