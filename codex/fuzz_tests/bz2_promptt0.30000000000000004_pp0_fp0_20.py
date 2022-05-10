import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as f:
    data = f.read(100)
    text = decompressor.decompress(data)
    print(text)

with open('data/enwik8.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    data = f.read(100)
    while data:
        text = decompressor.decompress(data)
        print(text)
        data = f.read(100)

with bz2.open('data/enwik8.bz2', 'rb') as f:
    data = f.read(100)
    print(data)

with bz2.open('data/enwik8.bz2', 'rt') as f:
    data = f.read(100)
    print(data)

# Test BZ2File
with bz2.open('data/enwik8.bz2', '
