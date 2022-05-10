import lzma
# Test LZMADecompressor.decompress()

# Test with a small input string
compressor = lzma.LZMACompressor()
data = b"Hello world! " * 10
compressed = compressor.compress(data)
compressed += compressor.flush()

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
print(decompressed)

# Test with a file
with open("/usr/share/dict/words", "rb") as f:
    data = f.read()

compressor = lzma.LZMACompressor()
compressed = compressor.compress(data)
compressed += compressor.flush()

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
print(decompressed)

# Test with a file-like object
with open("/usr/share/dict/words", "rb") as f:
    data = f.read()

compressor = lzma.LZMAComp
