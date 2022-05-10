import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
with open('test.bz2', 'rb') as f:
    data = decompressor.decompress(f.read())
    print(data)

# Test BZ2File
with bz2.BZ2File('test.bz2', 'rb') as f:
    data = f.read()
    print(data)
