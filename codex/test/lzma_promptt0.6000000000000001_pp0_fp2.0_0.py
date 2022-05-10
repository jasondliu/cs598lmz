import lzma
# Test LZMADecompressor with various filters.

def test_simple():
    data = b'\x00' * 10
