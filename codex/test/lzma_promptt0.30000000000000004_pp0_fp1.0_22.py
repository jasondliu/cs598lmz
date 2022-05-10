import lzma
# Test LZMADecompressor

with open('test.xz', 'rb') as f:
    d = lzma.LZMADecompressor()
