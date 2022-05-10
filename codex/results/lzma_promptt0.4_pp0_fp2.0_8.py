import lzma
# Test LZMADecompressor.
decomp = lzma.LZMADecompressor()
with open('lorem.xz', 'rb') as f:
    compressed = f.read()
    data = decomp.decompress(compressed)
    print(data)

# Test LZMAFile.
with lzma.open('lorem.xz', 'rb') as f:
    data = f.read()
    print(data)

# Test LZMAFile.
with lzma.open('lorem.xz', 'rb') as f:
    for line in f:
        print(line)

# Test LZMAFile.
with lzma.open('lorem.xz', 'rb') as f:
    data = f.read(10)
    print(data)
    print(f.tell())
    f.seek(0)
    print(f.tell())
    data = f.read(10)
    print(data)

# Test LZMAFile.
with lzma.open('lorem.xz', 'rb')
