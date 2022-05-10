import lzma
# Test LZMADecompressor

def test_lzma_decompressor_empty():
    d = lzma.LZMADecompressor()
    assert d.decompress(b"") == b""
    assert d.unused_data == b""
    assert d.eof == False

def test_lzma_decompressor_simple():
    d = lzma.LZMADecompressor()
    data = d.decompress(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x
