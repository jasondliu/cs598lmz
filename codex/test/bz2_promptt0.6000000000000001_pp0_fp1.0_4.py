import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()
original_data = b'This is the original text.'
compressed_data = bz2.compress(original_data)

print('Original:', len(original_data), original_data)
print('Compressed:', len(compressed_data), compressed_data)

# Decompress the compressed data.
decompressed_data = decompressor.decompress(compressed_data)

print('Decompressed:', len(decompressed_data), decompressed_data)

# Decompress the data incrementally.
decompressor = bz2.BZ2Decompressor()
decompressed_data = decompressor.decompress(compressed_data[:20])
decompressed_data += decompressor.decompress(compressed_data[20:])

print('Incremental:', len(decompressed_data), decompressed_data)

# Decompress the data in one step.
