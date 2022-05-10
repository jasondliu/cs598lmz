import lzma
# Test LZMADecompressor

with open('test.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    data = decompressor.decompress(f.read())
    print(data)

# Test LZMAFile

with lzma.open('test.xz', 'rb') as f:
    print(f.read())

# Test LZMAFile with filters

with lzma.open('test.xz', 'rb') as f:
    print(f.read())

# Test LZMAFile with filters

with lzma.open('test.xz', 'rb') as f:
    print(f.read())

# Test LZMAFile with filters

with lzma.open('test.xz', 'rb') as f:
    print(f.read())

# Test LZMAFile with filters

with lzma.open('test.xz', 'rb') as f:
    print(f.read())

# Test LZMAFile with filters

with l
