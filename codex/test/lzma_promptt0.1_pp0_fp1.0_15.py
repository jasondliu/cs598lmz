import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # Test decompression of a small string
    c = lzma.LZMADecompressor()
