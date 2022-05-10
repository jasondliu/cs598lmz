import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# Test BZ2File
bz2_file = bz2.BZ2File('compressed_file.bz2', 'wb')
bz2_file.write(original_data)
bz2_file.close()

bz2_file = bz2.BZ2File('compressed_file.bz2', 'rb')
print(bz2_file.read())
bz2_file.close()

# Test open()
with bz2.open('compressed_file.bz2', 'wt') as f:
    f.write(original_data)

with bz2.open('compressed_file.bz2', 'rt') as f:
    print(f.read())

# Test compress() and decompress()
compressed_data = bz2.compress(original_data)
print(bz2.decompress(compressed_data))
