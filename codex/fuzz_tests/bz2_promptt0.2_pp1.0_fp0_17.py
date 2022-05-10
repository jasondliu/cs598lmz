import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as f:
    data = f.read(1024)
    while data:
        print(decompressor.decompress(data))
        data = f.read(1024)

# Test BZ2File

with bz2.BZ2File('data/enwik8.bz2', 'rb') as f:
    data = f.read(1024)
    while data:
        print(data)
        data = f.read(1024)

# Test BZ2File with context manager

with bz2.BZ2File('data/enwik8.bz2', 'rb') as f:
    for line in f:
        print(line)

# Test BZ2File with context manager and readlines

with bz2.BZ2File('data/enwik8.bz2', 'rb') as f:
    for line in f.readlines():
        print(line)


