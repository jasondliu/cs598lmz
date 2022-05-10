import bz2
# Test BZ2Decompressor to decompress the data
b = bz2.BZ2Decompressor()
print(b.decompress(uncompressed_data).decode('utf-8'))

# Test BZ2File to decompress the data
b = bz2.BZ2File('compressed_data.bz2', 'r')
print(b.read().decode('utf-8'))

# Test BZ2File to compress the data
b = bz2.BZ2File('compressed_data.bz2', 'w')
b.write(uncompressed_data)
