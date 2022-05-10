import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/enwik8', 'rb') as f:
    data = f.read(100)
    print(decompressor.decompress(data))

with open('data/enwik8', 'rb') as f:
    for data in iter(lambda: f.read(100), b''):
        print(decompressor.decompress(data))

with open('data/enwik8', 'rb') as f:
    print(decompressor.decompress(f.read()))

with open('data/enwik8', 'rb') as f:
    print(decompressor.decompress(f.read(100)))

with open('data/enwik8', 'rb') as f:
    print(decompressor.decompress(f.read()))

with open('data/enwik8', 'rb') as f:
    print(decompressor.decompress(f.read(100)))

with open('data/enwik8',
