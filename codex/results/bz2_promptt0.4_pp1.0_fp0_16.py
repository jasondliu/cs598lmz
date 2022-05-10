import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
with open('data.bz2', 'rb') as f:
    data = f.read()
    print(decompressor.decompress(data))

# Test BZ2File
with bz2.BZ2File('data.bz2', 'rb') as f:
    print(f.read())

# Test compress
with open('data.bz2', 'wb') as f:
    f.write(bz2.compress(b'Hello World'))

# Test decompress
with open('data.bz2', 'rb') as f:
    print(bz2.decompress(f.read()))
