import bz2
# Test BZ2Decompressor

with open('../data/small.txt.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100), b''):
        print(decompressor.decompress(block))

print()

with open('../data/small.txt.bz2', 'rb') as f:
    for line in bz2.open(f):
        print(line)

print()

with open('../data/small.txt', 'rb') as f:
    for line in bz2.open(f):
        print(line)

print()

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()
with open('../data/small.txt', 'rb') as f:
    for block in iter(lambda: f.read(100), b''):
        print(compressor.compress(block))
    print(compressor.flush())

print()

with bz2.open('../data/
