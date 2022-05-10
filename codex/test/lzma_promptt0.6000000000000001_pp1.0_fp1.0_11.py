import lzma
# Test LZMADecompressor.decompress() with various input and output sizes.

def test(input, output, max_length=None, eof=True):
    c = lzma.LZMADecompressor()
    if max_length is None:
        max_length = len(output)
    result = c.decompress(input, max_length, eof)
    assert result == output

def test_large(input, output):
    c = lzma.LZMADecompressor()
    result = c.decompress(input)
    assert result == output

# Zero-length inputs and outputs.
