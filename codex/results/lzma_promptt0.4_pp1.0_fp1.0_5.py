import lzma
# Test LZMADecompressor

compressed = lzma.compress(b"Hello world!")
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
print(decompressed == b"Hello world!")

# Test LZMADecompressor with multiple calls to decompress()

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed[:-5])
decompressed += decompressor.decompress(compressed[-5:])
print(decompressed == b"Hello world!")

# Test LZMADecompressor with multiple calls to decompress() and
# unconsumed_tail

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed[:-5])
decompressed += decompressor.decompress(compressed[-5:])
print(decompressor.unconsumed_tail == b"")

# Test LZMADecompressor
