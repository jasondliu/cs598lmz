import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# Test BZ2File
bz_file = bz2.BZ2File('compressed_file.bz2', 'wb')
bz_file.write(original_data)
bz_file.close()
bz_file = bz2.BZ2File('compressed_file.bz2', 'rb')
bz_file.read()
bz_file.close()

# Test compress() and decompress()
compressed_data = bz2.compress(original_data)
decompressed_data = bz2.decompress(compressed_data)

# Test open()
bz2_file = bz2.open('compressed_file.bz2', mode='wt')
bz2_file.write(original_data)
bz2_file.close()
bz2_file = bz2.open('compressed_file.bz2', mode='rt')

