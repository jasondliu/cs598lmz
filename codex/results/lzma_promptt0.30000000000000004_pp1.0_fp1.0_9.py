import lzma
# Test LZMADecompressor

with open('data/lzma_compressed.bin', 'rb') as f:
    data = f.read()

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(data)
print(decompressed)

print(decompressor.eof)

# Test LZMACompressor

compressor = lzma.LZMACompressor()
compressed = compressor.compress(b'hello world')
compressed += compressor.flush()
print(compressed)

# Test LZMAFile

with lzma.open('data/lzma_compressed.bin', 'rb') as f:
    data = f.read()

print(data)

with lzma.open('data/lzma_compressed.bin', 'rb') as f:
    for line in f:
        print(line)

with lzma.open('data/lzma_compressed.bin', 'rb') as f:
    print(f.readline())


