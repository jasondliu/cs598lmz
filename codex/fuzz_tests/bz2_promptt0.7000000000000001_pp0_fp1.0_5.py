import bz2
# Test BZ2Decompressor
bz2_decompressor = bz2.BZ2Decompressor()
bz2_decompressor.decompress(compressed_data)
# Test BZ2File
with bz2.BZ2File('bz2_file', 'wb') as f:
    f.write(compressed_data)

with bz2.BZ2File('bz2_file', 'rb') as f:
    print(f.read())

os.remove('bz2_file')

print('-' * 80)

# bz2.compress() and bz2.decompress()
compressed_data = bz2.compress(data)
print(compressed_data)
print(bz2.decompress(compressed_data))

print('-' * 80)

# bz2.open()
with bz2.open('lorem_bz2.txt', 'wt') as f:
    f.write(data)

with bz2.open('lorem_bz2.txt', '
