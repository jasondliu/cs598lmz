import bz2
# Test BZ2Decompressor
with bz2.BZ2File('data/example4.bz2') as src, open('data/example5.txt', 'wt') as dst:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: src.read(100 * 1024), b''):
        dst.write(decompressor.decompress(block))
    dst.write(decompressor.flush())

# Test BZ2Compressor
with open('data/example5.txt', 'rt') as src, bz2.BZ2File('data/example6.bz2', 'wb') as dst:
    compressor = bz2.BZ2Compressor()
    for line in src:
        data = compressor.compress(line.encode('utf-8'))
        if data:
            dst.write(data)
    dst.write(compressor.flush())

# Test BZ2File
with bz2.BZ2File('data/example6.bz2') as f:
    print(f.readline())
