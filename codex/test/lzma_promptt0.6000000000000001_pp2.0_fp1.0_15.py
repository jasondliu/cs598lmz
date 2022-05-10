import lzma
# Test LZMADecompressor

def test_decompress():
    c = lzma.LZMADecompressor()
    assert c.decompress(b"") == b""
    assert c.unused_data == b""
    assert c.eof == False

    c = lzma.LZMADecompressor()
    assert c.decompress(b"Y" * 100) == b"Y" * 100
    assert c.unused_data == b""
    assert c.eof == False

    c = lzma.LZMADecompressor()
    assert c.decompress(b"Y" * 100 + lzma.endian_check()) == b"Y" * 100
    assert c.unused_data == lzma.endian_check()
    assert c.eof == False

    c = lzma.LZMADecompressor()
    assert c.decompress(lzma.endian_check()) == b""
    assert c.unused_data == lzma.endian_check()
