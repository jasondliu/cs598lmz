import lzma
# Test LZMADecompressor
with open('data/lzma_compressed.bin', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    data = decompressor.decompress(f.read())
    print(data)

# Test LZMACompressor
with open('data/lzma_compressed.bin', 'wb') as f:
    compressor = lzma.LZMACompressor()
    data = b"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    f.write(compressor.compress(data))
    f.write(compressor.flush())

# Test LZMADecompressor
with open('data/lzma_compressed.bin', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    data = decompressor.decompress(f.read())
    print(data)

# Test LZMADecompressor
with open('data/lzma_compressed.bin', 'rb') as f:
    decompressor = lzma
