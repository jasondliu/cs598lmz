import lzma
# Test LZMADecompressor without creating a decompressobj() first.
assert lzma.decompress(COMPRESSED_DATA) == SOURCE_DATA
