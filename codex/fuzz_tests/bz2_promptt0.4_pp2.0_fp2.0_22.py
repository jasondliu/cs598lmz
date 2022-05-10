import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# Test BZ2File
with bz2.BZ2File(filename, 'wb') as f:
    f.write(original_data)

with bz2.BZ2File(filename, 'rb') as f:
    print(f.read())

# Test compress()
with open(filename, 'wb') as f:
    f.write(bz2.compress(original_data))

with open(filename, 'rb') as f:
    print(bz2.decompress(f.read()))

# Test open()
with bz2.open(filename, 'wb') as f:
    f.write(original_data)

with bz2.open(filename, 'rb') as f:
    print(f.read())

# Test open() with compresslevel
with bz2.open(filename, 'wb', compresslevel=9) as f:
    f.write(original_data
