import bz2
# Test BZ2Decompressor
with bz2.BZ2File('data/test.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100 * decompressor.decompress(f.read(100))), b''):
        print(block)

# Test BZ2Compressor
with bz2.BZ2File('data/test.bz2', 'wb') as f:
    compressor = bz2.BZ2Compressor()
    for data in ['a', 'b', 'c']:
        f.write(compressor.compress(data))
        f.flush()
    f.write(compressor.flush())

# Test BZ2File
with bz2.BZ2File('data/test.bz2', 'r') as f:
    print(f.read())

# Test compress()/decompress()
print(bz2.decompress(bz2.compress('a')))
