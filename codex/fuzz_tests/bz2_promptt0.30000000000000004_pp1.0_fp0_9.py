import bz2
# Test BZ2Decompressor

with bz2.BZ2File('data/sample.bz2') as src, open('data/sample.out', 'wb') as dst:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: src.read(100 * 1024), b''):
        dst.write(decompressor.decompress(block))
    dst.write(decompressor.flush())

with open('data/sample.out', 'rb') as f:
    print(f.read())

# Test BZ2Compressor

with open('data/sample.out', 'rb') as src, bz2.BZ2File('data/sample.bz2.out', 'wb') as dst:
    compressor = bz2.BZ2Compressor()
    for block in iter(lambda: src.read(100 * 1024), b''):
        dst.write(compressor.compress(block))
    dst.write(compressor.flush())

with bz2.BZ2File('data/sample.bz2.
