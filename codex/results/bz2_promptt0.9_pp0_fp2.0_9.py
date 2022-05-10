import bz2
# Test BZ2Decompressor instance

# create some data to compress
original_data = b'This is the original text.'

print('original_data: {} bytes'.format(len(original_data)))
print(original_data)

compressor = bz2.BZ2Compressor()
compressed_data = compressor.compress(original_data)

#note that this data isn't complete
print('compressed_data: {} bytes'.format(len(compressed_data)))
print(compressed_data)

decompressor = bz2.BZ2Decompressor()
# breaks if the b'original_data' is not exist
result = decompressor.decompress(compressed_data)

# incomplete data raise error, when decompression is tried.
print('decompressed_data: {} bytes'.format(len(result)))
print(result)

# no data to decompress, returns empty byte string
print(decompressor.decompress(b''))

print(decompressor.decompress(b'BZh91AY&SY.\xaf\x82\r
