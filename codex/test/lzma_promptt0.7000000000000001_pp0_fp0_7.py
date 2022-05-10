import lzma
# Test LZMADecompressor.decompress
def test_decompress():
    c = lzma.LZMADecompressor()
    data = b"\x00" * 1000000
    assert c.decompress(data) == data
    assert c.eof is True
    assert c.unused_data == b""
    assert c.decompress(b"123") == b""

# Test LZMADecompressor.flush
def test_flush():
    c = lzma.LZMADecompressor()
    data = b"\x00" * 1000000
    with pytest.raises(EOFError):
        c.flush()
    c.decompress(data, 100000)
    assert c.flush() == data[100000:]
    assert c.eof is True
    assert c.unused_data == b""
    assert c.flush() == b""

# Test LZMADecompressor.copy
def test_copy():
    c = lzma.LZMADecompressor()
