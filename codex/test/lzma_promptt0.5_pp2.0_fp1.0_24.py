import lzma
# Test LZMADecompressor

lz = lzma.LZMADecompressor()

with open('test.xz', 'rb') as f:
    lz.decompress(f.read())

# Test LZMADecompressor.decompress

