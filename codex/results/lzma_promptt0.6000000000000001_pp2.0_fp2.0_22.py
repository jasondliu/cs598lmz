import lzma
# Test LZMADecompressor class

def test_decompressor_basic(size=1):
    c = lzma.LZMADecompressor()
    d = c.decompress(b'x' * size)
    assert d == b'x' * size

def test_decompressor_read():
    c = lzma.LZMADecompressor()
    d = c.decompress(b'x' * 2**14)
    assert d == b'x' * 2**14

def test_decompressor_readline():
    c = lzma.LZMADecompressor()
    d = c.decompress(b'x' * 2**14)
    assert d == b'x' * 2**14

def test_decompressor_readlines():
    c = lzma.LZMADecompressor()
    d = c.decompress(b'x' * 2**14)
    assert d == b'x' * 2**14

def test_decompressor_iter():
    c = lz
