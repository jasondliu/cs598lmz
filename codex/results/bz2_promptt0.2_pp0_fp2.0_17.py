import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/sample.bz2', 'rb') as f:
    file_content = f.read()
    print(decompressor.decompress(file_content))

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

uncompressed_data = b'This is the original text.'
compressed_data = compressor.compress(uncompressed_data)

print(compressed_data)

# Test BZ2File

with bz2.BZ2File('data/sample.bz2', 'rb') as f:
    file_content = f.read()
    print(file_content)

with bz2.BZ2File('data/sample.bz2', 'wb') as f:
    f.write(b'This is the original text.')

# Test BZ2Compressor.compress()

compressor = bz2.BZ2Compressor()

uncompressed_data
