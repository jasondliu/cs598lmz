import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as f:
    data = f.read(100)
    while data:
        print(decompressor.decompress(data))
        data = f.read(100)

print(decompressor.flush())

# Test BZ2File

with bz2.BZ2File('data/enwik8.bz2', 'rb') as f:
    data = f.read(100)
    while data:
        print(data)
        data = f.read(100)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('data/enwik8.bz2', 'rb') as f:
    data = f.read(100)
    while data:
        print(compressor.compress(data))
        data = f.read(100)

print(compressor.flush())

# Test BZ2File

with
