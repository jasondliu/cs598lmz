import lzma
# Test LZMADecompressor

def test_LZMADecompressor():
    # Test basic functionality
    d = lzma.LZMADecompressor()
    e = lzma.LZMADecompressor()
    assert d.decompress(b"") == b""
    assert d.unused_data == b""
    assert d.eof == False
    assert d.decompress(b"asdf") == b""
    assert d.unused_data == b"asdf"
    assert d.eof == False
    assert d.decompress(b"qwer") == b""
    assert d.unused_data == b"asdfqwer"
    assert d.eof == False
    assert d.decompress(b"") == b""
    assert d.unused_data == b"asdfqwer"
    assert d.eof == False
    assert d.decompress(b"zxcv") == b""
    assert d.unused_data == b"asdfqwerzxcv"
    assert d.e
