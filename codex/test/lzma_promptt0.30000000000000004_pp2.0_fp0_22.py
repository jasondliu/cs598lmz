import lzma
# Test LZMADecompressor

decompressor = lzma.LZMADecompressor()

with open('test.xz', 'rb') as f:
    data = f.read()

print(decompressor.decompress(data))

print(decompressor.unused_data)

# Test LZMACompressor

compressor = lzma.LZMACompressor()

with open('test.xz', 'rb') as f:
    data = f.read()

print(compressor.compress(data))

print(compressor.flush())

# Test LZMAFile

with lzma.open('test.xz', 'rb') as f:
    data = f.read()

print(data)

with lzma.open('test.xz', 'rt') as f:
    data = f.read()

print(data)

with lzma.open('test.xz', 'rb') as f:
    data = f.readlines()

print(data)

