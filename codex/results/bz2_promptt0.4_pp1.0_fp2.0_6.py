import bz2
# Test BZ2Decompressor
bz_decompressor = bz2.BZ2Decompressor()

result = bz_decompressor.decompress(compressed_data)

result == original_data

# Test BZ2File
uncompressed_file = bz2.BZ2File('uncompressed.txt', 'wb')
uncompressed_file.write(original_data)
uncompressed_file.close()

compressed_file = bz2.BZ2File('compressed.bz2', 'wb')
compressed_file.write(original_data)
compressed_file.close()

compressed_file = bz2.BZ2File('compressed.bz2', 'rb')
result = compressed_file.read()
compressed_file.close()

result == original_data

# Test BZ2Compressor
bz_compressor = bz2.BZ2Compressor()

result = bz_compressor.compress(original_data)
result += bz_compressor.flush()

result == compressed
