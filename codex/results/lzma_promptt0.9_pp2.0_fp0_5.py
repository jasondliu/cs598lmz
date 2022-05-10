import lzma
# Test LZMADecompressor.
# It must be eof to decompress from lzma.LZMAFile().
# See: https://bugs.python.org/issue28405
try:
    with lzma.LZMADecompressor() as d:
        d.decompress(b'x' * 10)
except lzma.LZMAError:
    pass
else:
    raise Exception("should raise LZMAError")

# Test LZMADecompressor.pop_stream.
# It must be eof before the last use of LZMADecompressor.
# See: https://bugs.python.org/issue28405
try:
    with lzma.LZMADecompressor() as d:
        d.decompress(b'x' * 10)
        d.pop_stream()
except lzma.LZMAError:
    pass
else:
    raise Exception("should raise LZMAError")

# It doesn't raise error when popleft_stream on empty.
d = lzma.LZMADecompressor
