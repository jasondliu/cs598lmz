import lzma
# Test LZMADecompressor

# Test that the decompressor can decompress a file compressed with the
# command-line utility.

with open('lzma_compat.xz', 'rb') as f:
    data = f.read()

decomp = lzma.LZMADecompressor()
decomp.decompress(data)

# Test that the decompressor can decompress a file compressed with the
# command-line utility and then compressed again with the decompressor.

with open('lzma_compat.xz', 'rb') as f:
    data = f.read()

decomp = lzma.LZMADecompressor()
data2 = decomp.decompress(data)

decomp = lzma.LZMADecompressor()
decomp.decompress(data2)

# Test that the decompressor can decompress a file compressed with the
# command-line utility and then compressed again with the decompressor,
# and that the decompressor can decompress the result again.

with open('lzma_compat.xz',
