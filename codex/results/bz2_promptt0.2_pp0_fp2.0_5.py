import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/sample.bz2', 'rb') as f:
    file_content = f.read()
    print(file_content)

decompressed_data = decompressor.decompress(file_content)
print(decompressed_data)

# Test BZ2File

with bz2.BZ2File('data/sample.bz2', 'rb') as f:
    file_content = f.read()
    print(file_content)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('data/sample.txt', 'rb') as f:
    file_content = f.read()
    compressed_data = compressor.compress(file_content)
    compressed_data += compressor.flush()
    print(compressed_data)

with open('data/sample.bz2', 'wb') as f:
    f.write(compressed_data)

# Test BZ2
