import bz2
# Test BZ2Decompressor
# Compress data
data = b'Lots of content here.'
compressor = bz2.BZ2Compressor()
compressed_data = compressor.compress(data)
compressed_data += compressor.flush()
print('Compressed is %d bytes' % len(compressed_data))
# Decompress data
decompressor = bz2.BZ2Decompressor()
decompressed_data = decompressor.decompress(compressed_data)
print('Decompressed is %d bytes' % len(decompressed_data))
print(decompressed_data)

# Test BZ2File
# Compress data
