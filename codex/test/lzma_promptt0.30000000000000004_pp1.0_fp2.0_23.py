import lzma
# Test LZMADecompressor.decompress()

def test_decompress():
    # Test with a small input string.
    d = lzma.LZMADecompressor()
