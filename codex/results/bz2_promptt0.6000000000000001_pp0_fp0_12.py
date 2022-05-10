import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()

# Decompress the compressed data
decompressed_data = decompressor.decompress(compressed_data)

# Finish decompression
decompressed_data += decompressor.flush()

# Print the len of the decompressed data
print('Decompressed is {} characters long.'.format(len(decompressed_data)))

# Decode the decompressed data
decoded_data = decompressed_data.decode('utf-8')

# Print the decoded data
print(decoded_data)
