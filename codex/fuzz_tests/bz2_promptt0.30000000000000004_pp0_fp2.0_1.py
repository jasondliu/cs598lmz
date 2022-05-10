import bz2
# Test BZ2Decompressor

bz2_decompressor = bz2.BZ2Decompressor()

with open('../data/enwik8.bz2', 'rb') as f:
    file_content = f.read()
    decompressed_data = bz2_decompressor.decompress(file_content)
    print(decompressed_data[:100])

# Test BZ2File

with bz2.BZ2File('../data/enwik8.bz2', 'rb') as f:
    file_content = f.read()
    print(file_content[:100])

# Test BZ2File with context manager

with bz2.BZ2File('../data/enwik8.bz2', 'rb') as f:
    for line in f:
        print(line[:100])
        break

# Test BZ2File with context manager and readlines

with bz2.BZ2File('../data/enwik8.bz2', 'rb') as f:
    lines = f.read
