import lzma
# Test LZMADecompressor
compressor = lzma.LZMACompressor()
data = compressor.compress(b'Hello World!')
data += compressor.flush()
print(data)
decompressor = lzma.LZMADecompressor()
print(decompressor.decompress(data))

# Test LZMADecompressor with multiple chunks
compressor = lzma.LZMACompressor()
data = compressor.compress(b'Hello World!')
data += compressor.flush()
print(data)
decompressor = lzma.LZMADecompressor()
print(decompressor.decompress(data[:5]))
print(decompressor.decompress(data[5:]))

# Test LZMADecompressor with multiple chunks and unconsumed data
compressor = lzma.LZMACompressor()
data = compressor.compress(b'Hello World!')
data += compressor.flush()
print(data)
decompressor = lzma.LZMADecompressor()
