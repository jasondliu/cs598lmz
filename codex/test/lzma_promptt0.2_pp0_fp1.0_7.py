import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # Test decompressor object
    c = lzma.LZMADecompressor()
    assert c.decompress(b"") == b""
    assert c.unused_data == b""
    assert c.eof is False
    assert c.decompress(b"x") == b""
    assert c.unused_data == b"x"
    assert c.eof is False
    assert c.decompress(b"x") == b""
    assert c.unused_data == b"x"
    assert c.eof is False
    assert c.decompress(b"y") == b""
    assert c.unused_data == b"xy"
    assert c.eof is False
    assert c.decompress(b"z") == b"x"
    assert c.unused_data == b"yz"
    assert c.eof is False
    assert c.decompress(b"") == b""
    assert c.unused_data == b
