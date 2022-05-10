import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/sample.bz2', 'rb') as f:
    file_content = f.read()
    print(decompressor.decompress(file_content))

# Test BZ2File

with bz2.BZ2File('data/sample.bz2') as f:
    file_content = f.read()
    print(file_content)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

uncompressed_data = b'This is the uncompressed data.'
compressed_data = compressor.compress(uncompressed_data)
print(compressed_data)

# Test BZ2File

with bz2.BZ2File('data/sample.bz2', 'w') as f:
    f.write(uncompressed_data)

# Test BZ2File with context manager

with bz2.BZ2File('data/sample.bz2', 'w
