import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as f:
    data = f.read()

decompressed = decompressor.decompress(data)

print(len(decompressed))

# Test BZ2File

with bz2.BZ2File('data/enwik8.bz2', 'rb') as f:
    data = f.read()

print(len(data))

# Test BZ2File with context manager

with bz2.BZ2File('data/enwik8.bz2', 'rb') as f:
    for line in f:
        print(line)
        break

# Test BZ2File with context manager and large buffer

with bz2.BZ2File('data/enwik8.bz2', 'rb') as f:
    for line in f:
        print(line)
        break

# Test BZ2File with context manager and large buffer

with bz2
