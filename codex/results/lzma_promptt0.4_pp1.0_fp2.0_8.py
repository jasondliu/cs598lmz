import lzma
# Test LZMADecompressor.decompress()

def test_decompress():
    d = lzma.LZMADecompressor()
    assert d.decompress(b"") == b""
    assert d.decompress(b"x") == b"x"
    assert d.decompress(b"xy") == b"xy"
    assert d.decompress(b"xyz") == b"xyz"
    assert d.decompress(b"xyz" * 100) == b"xyz" * 100
    assert d.decompress(b"xyz" * 100 + b"abc") == b"xyz" * 100 + b"abc"
    assert d.decompress(b"xyz" * 100 + b"abc", max_length=200) == b"xyz" * 100 + b"abc"
    assert d.decompress(b"xyz" * 100 + b"abc", max_length=100) == b"xyz" * 100
    raises(lzma.LZMAError, d.decompress, b"
