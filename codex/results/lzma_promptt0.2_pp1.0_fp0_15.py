import lzma
# Test LZMADecompressor

decompressor = lzma.LZMADecompressor()

with open('test.xz', 'rb') as f:
    data = f.read()
    print(decompressor.decompress(data))

# Test LZMAFile

with lzma.open('test.xz', 'rb') as f:
    print(f.read())

# Test LZMAFile with filters

with lzma.open('test.xz', 'rb') as f:
    print(f.read())

# Test LZMAFile with filters and preset

with lzma.open('test.xz', 'rb') as f:
    print(f.read())

# Test LZMAFile with filters and preset and check

with lzma.open('test.xz', 'rb') as f:
    print(f.read())

# Test LZMAFile with filters and preset and check and format

with lzma.open('test.xz', 'rb') as f:
    print(f.read())
