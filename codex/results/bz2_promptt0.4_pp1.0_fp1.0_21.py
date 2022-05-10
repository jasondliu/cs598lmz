import bz2
# Test BZ2Decompressor
with bz2.BZ2File('data/test.bz2') as f:
    print(f.read())

with bz2.BZ2File('data/test.bz2') as f:
    decompressor = bz2.BZ2Decompressor()
    print(decompressor.decompress(f.read()))

decompressor = bz2.BZ2Decompressor()
with open('data/test.bz2', 'rb') as f:
    for block in iter(lambda: f.read(100), b''):
        print(decompressor.decompress(block))

with open('data/test.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    with open('data/test.out', 'wb') as g:
        for block in iter(lambda: f.read(100), b''):
            g.write(decompressor.decompress(block))

# Compress data in memory
data = b'Lots of data here
