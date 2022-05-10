import lzma
# Test LZMADecompressor
with open('test.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
