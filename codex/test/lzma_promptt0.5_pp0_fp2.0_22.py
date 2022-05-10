import lzma
# Test LZMADecompressor.decompress() with multiple chunks of data.

def test_decompress_multiple_chunks():
    c = lzma.LZMADecompressor()
