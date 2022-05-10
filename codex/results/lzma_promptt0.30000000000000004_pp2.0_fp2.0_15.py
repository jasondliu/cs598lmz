import lzma
# Test LZMADecompressor

with open('lzma_compressed.bin', 'rb') as f:
    compressed = f.read()

decompressor = lzma.LZMADecompressor()

with open('lzma_decompressed.bin', 'wb') as f:
    f.write(decompressor.decompress(compressed))

# Test LZMADecompressor.decompress()

with open('lzma_compressed.bin', 'rb') as f:
    compressed = f.read()

decompressed = lzma.decompress(compressed)

with open('lzma_decompressed.bin', 'wb') as f:
    f.write(decompressed)

# Test LZMAFile

with lzma.open('lzma_compressed.bin', 'rb') as f:
    decompressed = f.read()

with open('lzma_decompressed.bin', 'wb') as f:
    f.write(decompressed)

# Test LZMAFile
