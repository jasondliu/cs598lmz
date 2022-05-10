import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as f:
    data = f.read(100)
    while data:
        print(decompressor.decompress(data))
        data = f.read(100)

# Test BZ2File
with bz2.BZ2File('data/enwik8.bz2', 'r') as f:
    print(f.read(100))

# Test bz2.open
with bz2.open('data/enwik8.bz2', 'r') as f:
    print(f.read(100))

# Test bz2.compress
data = b'Hello World!'
compressed = bz2.compress(data)
print(compressed)
print(bz2.decompress(compressed))

# Test bz2.compresslevel
for i in range(10):
    print('compresslevel', i, len(bz2.compress(data, compress
