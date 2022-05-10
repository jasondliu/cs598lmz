import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/sample.bz2', 'rb') as f:
    data = f.read()

decompressed_data = decompressor.decompress(data)

print(decompressed_data)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('data/sample.bz2', 'rb') as f:
    data = f.read()

compressed_data = compressor.compress(data)

print(compressed_data)

# Test BZ2File

with bz2.BZ2File('data/sample.bz2', 'rb') as f:
    data = f.read()

print(data)

# Test BZ2File with context manager

with bz2.BZ2File('data/sample.bz2', 'rb') as f:
    for line in f:
        print(line)

# Test BZ2File with context manager and read
