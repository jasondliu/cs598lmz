import bz2
# Test BZ2Decompressor
bz_decompress = bz2.BZ2Decompressor()
uncompressed_data = bz_decompress.decompress(compressed_data)
uncompressed_data == data

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
compressor.compress(data)
compressor.flush()
compressed_data = compressor.compress(data) + compressor.flush()
compressed_data == data

# Test BZ2File
with open('data.bz2', 'wb') as bz2_file:
    bz2_file.write(compressed_data)

with bz2.BZ2File('data.bz2', 'rb') as bz2_file:
    uncompressed_data = bz2_file.read()
    uncompressed_data == data

# Test compress() and decompress()
compressed_data = bz2.compress(data)
uncompressed_data = bz2.decompress(compressed_data)

# Test
