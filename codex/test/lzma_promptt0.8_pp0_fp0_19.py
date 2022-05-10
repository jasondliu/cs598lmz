import lzma
# Test LZMADecompressor class
d = lzma.LZMADecompressor()
with open('sample.xz', 'rb') as f:
    f.seek(10)
