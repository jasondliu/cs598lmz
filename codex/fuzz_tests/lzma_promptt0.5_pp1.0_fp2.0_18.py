import lzma
# Test LZMADecompressor

decompressor = lzma.LZMADecompressor()

with open('test_data/lzma_compressed.xz', 'rb') as f:
    compressed_data = f.read()

decompressed_data = decompressor.decompress(compressed_data)

print('Original:', len(decompressed_data))
print(decompressed_data[:80])

compressed = lzma.compress(decompressed_data)
print('Compressed:', len(compressed))

compressor = lzma.LZMACompressor()
compressed = compressor.compress(decompressed_data)
compressed += compressor.flush()
print('Compressed:', len(compressed))

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
print('Decompressed:', len(decompressed))

print(decompressed == decompressed_data)

compressor = lzma.LZMACompressor()

