import bz2
# Test BZ2Decompressor
bz2_decompressor = bz2.BZ2Decompressor()
bz2_decompressor.decompress(bz2_compressed)

# Test BZ2File
with bz2.BZ2File('bz2_file.bz2', 'wb') as f:
    f.write(bz2_compressed)

with bz2.BZ2File('bz2_file.bz2', 'rb') as f:
    print(f.read())

# Test bz2.compress()
bz2_compressed = bz2.compress(text)
print(bz2_compressed)

# Test bz2.decompress()
bz2.decompress(bz2_compressed)

# Test bz2.open()
with bz2.open('bz2_file.bz2', 'wb') as f:
    f.write(bz2_compressed)

with bz2.open('bz2_file.bz2',
