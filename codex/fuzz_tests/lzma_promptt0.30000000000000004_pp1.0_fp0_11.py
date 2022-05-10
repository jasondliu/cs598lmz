import lzma
# Test LZMADecompressor
with open('data/lzma_compressed.bin', 'rb') as f:
    data = f.read()

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(data)
print(decompressed)

# Test LZMACompressor
compressor = lzma.LZMACompressor()
compressed = compressor.compress(b'Hello world!')
compressed += compressor.flush()
print(compressed)

# Test LZMADecompressor.decompress()
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
print(decompressed)

# Test LZMADecompressor.__call__()
decompressor = lzma.LZMADecompressor()
decompressed = decompressor(compressed)
print(decompressed)

# Test LZMADecompressor.decompress() with multiple chunks
decompressor = lzma.LZ
