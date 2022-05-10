import lzma
# Test LZMADecompressor
compressor = lzma.LZMACompressor()
data = compressor.compress(b'Hello world!')
data += compressor.flush()

decompressor = lzma.LZMADecompressor()
print(decompressor.decompress(data))

# Test LZMADecompressor.decompress()
decompressor = lzma.LZMADecompressor()
