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
test(b'', b'')
test(b'', b'', 0)
test(b'', b'', 1)
test(b'', b'', 2)
test(b'', b'', 3)
test(b'', b'', 4)
test(b'', b'', 5)
test(b'', b'', 6)
test(b'', b'', 7)
test(b'', b'', 8)

