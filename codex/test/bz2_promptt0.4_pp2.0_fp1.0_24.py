import bz2
# Test BZ2Decompressor

with open('test.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    data = f.read()
    print(decompressor.decompress(data))

# Test BZ2File

with bz2.BZ2File('test.bz2', 'r') as f:
    print(f.read())

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()
compressed_data = compressor.compress(b'Hello World!')
compressed_data += compressor.flush()
print(compressed_data)

# Test BZ2File

with bz2.BZ2File('test.bz2', 'w') as f:
    f.write(b'Hello World!')

# Test BZ2File

with bz2.BZ2File('test.bz2', 'w') as f:
    f.write(b'Hello World!')

# Test BZ2File

