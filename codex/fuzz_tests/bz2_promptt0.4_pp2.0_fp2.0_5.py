import bz2
# Test BZ2Decompressor

decomp = bz2.BZ2Decompressor()

with open('data/enwik8', 'rb') as f:
    data = f.read(1024)
    while data:
        print(decomp.decompress(data))
        data = f.read(1024)

print(decomp.flush())

# Test BZ2Compressor

comp = bz2.BZ2Compressor()

with open('data/enwik8', 'rb') as f:
    data = f.read(1024)
    while data:
        print(comp.compress(data))
        data = f.read(1024)

print(comp.flush())

# Test compress() and decompress()

with open('data/enwik8', 'rb') as f:
    data = f.read(1024)
    while data:
        print(bz2.decompress(bz2.compress(data)))
        data = f.read(1024)

# Test BZ2File

with bz2.BZ2File
