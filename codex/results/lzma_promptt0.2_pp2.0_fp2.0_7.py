import lzma
# Test LZMADecompressor

decompressor = lzma.LZMADecompressor()

with open('lzma_compressed.bin', 'rb') as f:
    data = f.read()

decompressed = decompressor.decompress(data)

print(decompressed)

# Test LZMACompressor

compressor = lzma.LZMACompressor()

with open('lzma_compressed.bin', 'wb') as f:
    f.write(compressor.compress(b'Hello World!'))
    f.write(compressor.flush())

with open('lzma_compressed.bin', 'rb') as f:
    data = f.read()

decompressed = decompressor.decompress(data)

print(decompressed)

# Test LZMADecompressor.format

decompressor = lzma.LZMADecompressor()

with open('lzma_compressed.bin', 'rb') as f:
    data = f.read()

decomp
