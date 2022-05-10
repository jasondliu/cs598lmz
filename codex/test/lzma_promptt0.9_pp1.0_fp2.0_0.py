import lzma
# Test LZMADecompressor and LZMACompressor
assert lzma.decompress(lzma.compress(b'foo')) == b'foo'
