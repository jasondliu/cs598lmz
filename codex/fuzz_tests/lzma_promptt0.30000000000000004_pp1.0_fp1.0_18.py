import lzma
# Test LZMADecompressor.decompress()

# Test decompressing a file
with open('testdata/compressed-text.xz', 'rb') as f:
    with lzma.open(f, 'rb') as xf:
        data = xf.read()
        assert data == b'The quick brown fox jumps over the lazy dog.\n'

# Test decompressing a file with multiple concatenated streams
with open('testdata/compressed-text-multiple.xz', 'rb') as f:
    with lzma.open(f, 'rb') as xf:
        data = xf.read()
        assert data == b'The quick brown fox jumps over the lazy dog.\n' * 3

# Test decompressing a file with multiple concatenated streams
# and a trailing garbage byte
with open('testdata/compressed-text-multiple-trailing-garbage.xz', 'rb') as f:
    with lzma.open(f, 'rb') as xf:
        data = xf.read()
        assert data == b'The quick brown fox jumps
