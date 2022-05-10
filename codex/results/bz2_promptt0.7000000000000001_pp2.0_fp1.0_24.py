import bz2
# Test BZ2Decompressor
# test_decompressor = bz2.BZ2Decompressor()
# test_data = open('test.bz2', 'rb').read()
# decompressed_data = test_decompressor.decompress(test_data)
# print(decompressed_data)

# Test BZ2Compressor
test_compressor = bz2.BZ2Compressor()
test_data = open('test.bz2', 'rb').read()
compressed_data = test_compressor.compress(test_data)
print(compressed_data)
