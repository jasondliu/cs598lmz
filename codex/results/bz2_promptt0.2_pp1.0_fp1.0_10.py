import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as f:
    data = f.read(100)
    while data:
        print(decompressor.decompress(data))
        data = f.read(100)

# Test BZ2File

with bz2.BZ2File('data/enwik8.bz2') as f:
    print(f.read(100))

# Test BZ2File with context manager

with bz2.BZ2File('data/enwik8.bz2') as f:
    for line in f:
        print(line)
        break

# Test BZ2File with context manager and readlines

with bz2.BZ2File('data/enwik8.bz2') as f:
    print(f.readlines())

# Test BZ2File with context manager and readline

with bz2.BZ2File('data/enwik8.bz2')
