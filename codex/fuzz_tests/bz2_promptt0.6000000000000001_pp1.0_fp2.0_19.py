import bz2
# Test BZ2Decompressor

# compress data
bz2_compressor = bz2.BZ2Compressor(9)
data_compressed = bz2_compressor.compress(data)
data_compressed += bz2_compressor.flush()

# decompress data
bz2_decompressor = bz2.BZ2Decompressor()
data_decompressed = bz2_decompressor.decompress(data_compressed)

# check
assert data_decompressed == data
 
# Test BZ2File

# compress data
file_compressed = bz2.BZ2File('file_compressed.bz2', 'w')
file_compressed.write(data)
file_compressed.close()

# decompress data
file_decompressed = bz2.BZ2File('file_compressed.bz2', 'r')
data_decompressed = file_decompressed.read()
file_decompressed.close()

# check
assert data_decompressed == data
 
# Test
