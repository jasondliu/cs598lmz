import bz2
# Test BZ2Decompressor

with open('sample.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    with open('sample.txt', 'wb') as f2:
        for data in iter(lambda: f.read(100 * 1024), b''):
            f2.write(decompressor.decompress(data))

# Test BZ2Compressor

with open('sample.txt', 'rb') as f:
    compressor = bz2.BZ2Compressor()
    with open('sample.bz2', 'wb') as f2:
        for data in iter(lambda: f.read(100 * 1024), b''):
            f2.write(compressor.compress(data))
        f2.write(compressor.flush())
 
# Test BZ2File

with bz2.BZ2File('sample.bz2', 'rb') as f:
    with open('sample.txt', 'wb') as f2:
        f2.write(f.read())

with open('sample.
