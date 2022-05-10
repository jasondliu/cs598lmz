import lzma
# Test LZMADecompressor

with lzma.open('data/python.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    decompressed_data = decompressor.decompress(f.read())
    print(decompressed_data)

# Test LZMACompressor

compressor = lzma.LZMACompressor()
compressed_data = compressor.compress(b'This is some data')
compressed_data += compressor.flush()
print(compressed_data)

# Test LZMAFile

with lzma.open('data/python.xz', 'rb') as f:
    print(f.read())

with lzma.open('data/python.xz', 'rb') as f:
    print(f.readline())

with lzma.open('data/python.xz', 'rb') as f:
    for line in f:
        print(line)

with lzma.open('data/python.xz', 'rb') as f:
    print
