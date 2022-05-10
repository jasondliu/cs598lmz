import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('example.bz2', 'rb') as f:
    file_content = f.read()
    decompressed_data = decompressor.decompress(file_content)
    print(decompressed_data)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

uncompressed_data = b'This is the uncompressed data.'
compressed_data = compressor.compress(uncompressed_data)

print(compressed_data)

# A bzip2 file can contain multiple concatenated compressed streams.

compressor = bz2.BZ2Compressor()

uncompressed_data = b'This is the uncompressed data. '
compressed_data = compressor.compress(uncompressed_data)

print(compressed_data)

compressed_data += compressor.flush()

print(compressed_data)

# Compressing and Decompressing Files

