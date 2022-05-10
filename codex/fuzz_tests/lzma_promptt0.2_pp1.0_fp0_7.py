import lzma
# Test LZMADecompressor.decompress()

# Test decompressing a file with a single chunk
with open('testdata/lzma-single-chunk.xz', 'rb') as f:
    c = lzma.LZMADecompressor()
    data = c.decompress(f.read())
    assert data == b'foobar'

# Test decompressing a file with multiple chunks
with open('testdata/lzma-multiple-chunks.xz', 'rb') as f:
    c = lzma.LZMADecompressor()
    data = c.decompress(f.read())
    assert data == b'foobar'

# Test decompressing a file with multiple chunks and a size limit
with open('testdata/lzma-multiple-chunks.xz', 'rb') as f:
    c = lzma.LZMADecompressor()
    data = c.decompress(f.read(), max_length=3)
    assert data == b'foo'

# Test decompressing a file with multiple chunks and a
