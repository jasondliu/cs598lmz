import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# Test BZ2File
bz2_file = bz2.BZ2File('file.bz2', 'wb')
bz2_file.write(original_data)
bz2_file.close()

bz2_file = bz2.BZ2File('file.bz2', 'rb')
print(bz2_file.read())
bz2_file.close()

# Test compress and decompress
print(bz2.decompress(bz2.compress(original_data)))

# Test open
bz2_file = bz2.open('file.bz2', 'wt')
bz2_file.write(original_data)
bz2_file.close()

bz2_file = bz2.open('file.bz2', 'rt')
print(bz2_file.read())
bz2_file.close()
