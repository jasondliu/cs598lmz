import lzma
# Test LZMADecompressor.
assert lzma.decompress(lzma.compress(b"xyz")) == b"xyz"
# Test LZMACompressor.
c = lzma.LZMACompressor()
