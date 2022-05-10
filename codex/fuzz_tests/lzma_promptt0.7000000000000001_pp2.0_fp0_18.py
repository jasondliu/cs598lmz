import lzma
# Test LZMADecompressor.flush()

# Check that flush() returns an empty bytes object when the stream is
# fully decompressed.

dec = lzma.LZMADecompressor()
with open('testdata/lzma.lzma', 'rb') as f:
    data = f.read()

assert dec.decompress(data) == b'1234567890'
assert dec.flush() == b''

# Check that flush() returns an empty bytes object when the stream is
# partially decompressed.

dec = lzma.LZMADecompressor()
with open('testdata/lzma.lzma', 'rb') as f:
    data = f.read()

assert dec.decompress(data[:100]) == b'1234567890'[:100]
assert dec.flush() == b''

# Check that decompress() raises an EOFError when the stream is
# truncated.

dec = lzma.LZMADecompressor()
with open('testdata/lzma.lzma', 'rb')
