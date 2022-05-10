import lzma
# Test LZMADecompressor
assert LZMADecompressor().decompress(b"\x00") == b""
# Test LZMACompressor
lzma_compressor = LZMACompressor()
lzma_compressob = lzma.LZMACompressor()

data = bytes(range(256)) * 1000

compressed1 = lzma_compressor.compress(data)
compressed1 += lzma_compressor.flush()

compressed2 = lzma_compressob.compress(data)
compressed2 += lzma_compressob.flush()

# Compare with the lzma module
assert compressed1 == compressed2
