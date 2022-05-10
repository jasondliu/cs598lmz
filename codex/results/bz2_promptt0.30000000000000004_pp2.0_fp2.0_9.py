import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
with open('data/enwik8.bz2', 'rb') as f:
    data = f.read(100)
    print(decompressor.decompress(data))

# Test BZ2File
with bz2.BZ2File('data/enwik8.bz2', 'r') as f:
    print(f.read(100))

# Test open
with bz2.open('data/enwik8.bz2', 'r') as f:
    print(f.read(100))

# Test compress
with open('data/enwik8.bz2', 'rb') as f:
    data = f.read(100)
    print(bz2.decompress(data))

# Test decompress
with open('data/enwik8.bz2', 'rb') as f:
    data = f.read(100)
    print(bz2.decompress(data))

# Test compress
with open('data/enwik
