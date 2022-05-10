import lzma
# Test LZMADecompressor

decompressor = lzma.LZMADecompressor()

with open('data/lzma_compressed.bin', 'rb') as f:
    data = f.read()

decompressed = decompressor.decompress(data)

print(decompressed)

# Test LZMACompressor

compressor = lzma.LZMACompressor()

with open('data/lzma_compressed.bin', 'wb') as f:
    f.write(compressor.compress(b'Hello world!'))
    f.write(compressor.flush())

# Test LZMADecompressor.decompress()

with open('data/lzma_compressed.bin', 'rb') as f:
    data = f.read()

decompressed = lzma.decompress(data)

print(decompressed)

# Test LZMACompressor.compress()

with open('data/lzma_compressed.bin', 'wb') as f:
    f.write
