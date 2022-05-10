import bz2
bz2.decompress(compressed_data)

# bz2.compress()

bz2_compressor = bz2.BZ2Compressor()
result = bz2_compressor.compress(data)
result += bz2_compressor.flush()

# bz2.BZ2Compressor

bz2_compressor = bz2.BZ2Compressor()
result = bz2_compressor.compress(data)
result += bz2_compressor.flush()

# bz2.BZ2Decompressor

bz2_decompressor = bz2.BZ2Decompressor()
result = bz2_decompressor.decompress(compressed_data)

# bz2.BZ2File

bz2_file = bz2.BZ2File('file.bz2', 'wb')
try:
    bz2_file.write(data)
finally:
    bz2_file.close()

bz2_file = bz2
