import lzma
# Test LZMADecompressor

# Test decompression of a simple file
with open('test/data/lzma/lzma_alone_decompress.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    data = decompressor.decompress(f.read())
    assert data == b'This is a test of the LZMA decompressor.\n'

# Test decompression of a file with a header
with open('test/data/lzma/lzma_alone_decompress.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    data = decompressor.decompress(f.read())
    assert data == b'This is a test of the LZMA decompressor.\n'

# Test decompression of a file with a header and a footer
with open('test/data/lzma/lzma_alone_decompress.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
