import lzma
# Test LZMADecompressor

compressor = lzma.LZMACompressor()
decompressor = lzma.LZMADecompressor()

data = b'This is the original text.'
compressed = compressor.compress(data)
compressed += compressor.flush()

print('Original:', data)
print('Compressed:', compressed)

decompressed = decompressor.decompress(compressed)
print('Decompressed:', decompressed)

# Test LZMADecompressor with multiple calls to decompress()

compressor = lzma.LZMACompressor()
decompressor = lzma.LZMADecompressor()

data = b'This is the original text.'
compressed = compressor.compress(data)
compressed += compressor.flush()

decompressed1 = decompressor.decompress(compressed[:5])
decompressed2 = decompressor.decompress(compressed[5:])

print('Decompressed:', decompressed1 + decompressed2)

# Test LZMADecompressor
