import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# Test BZ2File
bz2_file = bz2.BZ2File('file.bz2', 'wb')
bz2_file.write(data)
bz2_file.close()

bz2_file = bz2.BZ2File('file.bz2', 'rb')
print(bz2_file.read())
bz2_file.close()

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
compressor.compress(data)
compressor.flush()

# Test BZ2File
bz2_file = bz2.BZ2File('file.bz2', 'wb')
bz2_file.write(data)
bz2_file.close()

bz2_file = bz2.BZ2File('file.bz2', 'rb')
print(bz2_file.read
