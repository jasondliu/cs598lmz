import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/sample.bz2', 'rb') as f:
    file_content = f.read()
    print(decompressor.decompress(file_content))

# Test BZ2File

with bz2.BZ2File('data/sample.bz2', 'rb') as f:
    file_content = f.read()
    print(file_content)

# Test BZ2File with context manager

with bz2.BZ2File('data/sample.bz2', 'rb') as f:
    for line in f:
        print(line)

# Compress data

data = b'Lots of data here.'
compressed = bz2.compress(data)
print(compressed)

# Compress data with context manager

with bz2.BZ2File('data/compressed.bz2', 'wb') as f:
    f.write(data)

# Compress data with context manager

with
