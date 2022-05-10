import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('sample.bz2', 'rb') as f:
    file_content = f.read()
    print(decompressor.decompress(file_content))

print(decompressor.unused_data)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('sample.txt', 'rb') as f:
    file_content = f.read()
    compressed_content = compressor.compress(file_content)
    compressed_content += compressor.flush()

print(compressed_content)

print(compressor.unused_data)

# Test BZ2File

with bz2.BZ2File('sample.bz2', 'rb') as f:
    file_content = f.read()
    print(file_content)

with bz2.BZ2File('sample.bz2', 'wb') as f:
    f.write(b'Hello World!')


