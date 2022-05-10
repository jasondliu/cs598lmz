import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/sample.bz2', 'rb') as f:
    file_content = f.read()
    print(decompressor.decompress(file_content))

# Test BZ2File

with bz2.BZ2File('data/sample.bz2', 'rb') as f:
    print(f.read())

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

uncompressed_data = b'This is the original text.'
compressed_data = compressor.compress(uncompressed_data)
print(compressed_data)

# Test BZ2File

with bz2.BZ2File('data/compressed_file.bz2', 'wb') as f:
    f.write(uncompressed_data)

with bz2.BZ2File('data/compressed_file.bz2', 'rb') as f:
    print(f.read())

