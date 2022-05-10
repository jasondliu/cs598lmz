import lzma
# Test LZMADecompressor

with open('test.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    data = f.read(10)
    while data:
        print(decompressor.decompress(data))
        data = f.read(10)

print(decompressor.unused_data)

decompressor = lzma.LZMADecompressor()

with open('test.xz', 'rb') as f:
    data = f.read(10)
    while data:
        print(decompressor.decompress(data))
        data = f.read(10)

print(decompressor.unused_data)

decompressor = lzma.LZMADecompressor()

with open('test.xz', 'rb') as f:
    data = f.read(10)
    while data:
        print(decompressor.decompress(data))
        data = f.read(10)

print(decompressor.unused_data
