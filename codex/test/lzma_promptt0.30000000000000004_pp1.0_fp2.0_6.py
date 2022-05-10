import lzma
# Test LZMADecompressor

with open('test.xz', 'rb') as f:
    d = lzma.LZMADecompressor()
    data = f.read()
    print(d.decompress(data))

# Test LZMAFile

with lzma.open('test.xz', 'rb') as f:
    print(f.read())

# Test LZMAFile with filters

