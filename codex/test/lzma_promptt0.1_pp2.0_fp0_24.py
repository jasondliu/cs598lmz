import lzma
# Test LZMADecompressor

with open('test.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    data = f.read(10)
    while data:
        print(decompressor.decompress(data))
        data = f.read(10)

# Test LZMAFile

with lzma.open('test.xz', 'rb') as f:
    print(f.read())

# Test LZMAFile with filters

