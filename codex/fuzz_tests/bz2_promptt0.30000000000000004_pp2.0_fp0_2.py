import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# Test BZ2File
bz2_file = bz2.BZ2File('example.bz2', 'wb')
bz2_file.write(original_data)
bz2_file.close()

bz2_file = bz2.BZ2File('example.bz2', 'rb')
print(bz2_file.read())
bz2_file.close()

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
compressor.compress(original_data)
compressor.flush()

# Test BZ2File
bz2_file = bz2.BZ2File('example.bz2', 'wb')
bz2_file.write(original_data)
bz2_file.close()

bz2_file = bz2.BZ2File('example.bz2', 'rb')
print(b
