import lzma
# Test LZMADecompressor

def test_LZMADecompressor_read():
    # Test LZMADecompressor.read()
    d = lzma.LZMADecompressor()
    assert d.read(1) == b""
    assert d.read(1) == b""
    assert d.read(1) == b""
    assert d.read(1) == b""
    assert d.read(10) == b""
    assert d.read(10) == b""
    assert d.read(10) == b""
    assert d.read(10) == b""
    assert d.read(100) == b""
    assert d.read(100) == b""
    assert d.read(100) == b""
    assert d.read(100) == b""
    assert d.read(0) == b""
    assert d.read() == b""
    assert d.read() == b""
    assert d.read() == b""
    assert d.read() == b""
    assert d.read() == b""
