import bz2
# Test BZ2Decompressor

decomp = bz2.BZ2Decompressor()

with open('enwik9') as f:
    data = f.read(100)
    while data:
        print(decomp.decompress(data))
        data = f.read(100)

# Test BZ2Compressor

comp = bz2.BZ2Compressor()

with open('enwik9') as f:
    data = f.read(100)
    while data:
        print(comp.compress(data))
        data = f.read(100)

print(comp.flush())

# Test BZ2File

with bz2.BZ2File('enwik9.bz2', 'w') as f:
    f.write(b'Hello, world!')

with bz2.BZ2File('enwik9.bz2', 'r') as f:
    print(f.read())

# Test BZ2File with context manager

with bz2.BZ2File('enwik9.bz2
