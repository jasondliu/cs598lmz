import bz2
# Test BZ2Decompressor
with bz2.BZ2File('data/sample.bz2', 'r') as f:
    print(f.read())

with open('data/sample.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    print(decompressor.decompress(f.read()))

with open('data/sample.bz2', 'rb') as f:
    print(bz2.decompress(f.read()))

# Test BZ2Compressor
with bz2.BZ2File('data/sample.bz2.out', 'w') as f:
    f.write(b'Hello World!')

with open('data/sample.bz2.out', 'rb') as f:
    print(f.read())

compressor = bz2.BZ2Compressor()
with open('data/sample.bz2.out', 'wb') as f:
    f.write(compressor.compress(b'Hello World!'))
    f.write
