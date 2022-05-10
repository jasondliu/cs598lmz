import lzma
# Test LZMADecompressor class

decomp = lzma.LZMADecompressor()

with open('lzma_compressed.bin', 'rb') as f:
    compressed = f.read()

decompressed = decomp.decompress(compressed)

print(decompressed)

print(decompressed.decode())

# Test LZMADecompressor class

decomp = lzma.LZMADecompressor()

with open('lzma_compressed.bin', 'rb') as f:
    compressed = f.read()

decompressed = decomp.decompress(compressed)

print(decompressed)

print(decompressed.decode())

# Test LZMADecompressor class

decomp = lzma.LZMADecompressor()

with open('lzma_compressed.bin', 'rb') as f:
    compressed = f.read()

decompressed = decomp.decompress(compressed)

print(decompressed)

print(dec
