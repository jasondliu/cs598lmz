import lzma
# Test LZMADecompressor.__init__()

def test_lzma_init():
    d = lzma.LZMADecompressor()
    assert d.eof is False
    assert d.unused_data == b""
    assert d.unconsumed_tail == b""
    # Test LZMADecompressor.decompress()

def test_lzma_decompress():
    # Test decompression of a simple string
    d = lzma.LZMADecompressor()
    data = d.decompress(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
