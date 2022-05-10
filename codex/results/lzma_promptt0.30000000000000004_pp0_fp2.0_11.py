import lzma
# Test LZMADecompressor

# Test that the decompressor can decompress a file compressed with the
# lzma module

with open("testdata/lzma_compressed", "rb") as f:
    compressed = f.read()

with lzma.open("testdata/lzma_compressed", "rb") as f:
    uncompressed = f.read()

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)

assert decompressed == uncompressed

# Test that the decompressor can decompress a file compressed with the
# xz command line tool

with open("testdata/xz_compressed", "rb") as f:
    compressed = f.read()

with lzma.open("testdata/xz_compressed", "rb") as f:
    uncompressed = f.read()

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)

assert decompressed == uncompressed

# Test that
