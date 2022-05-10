import bz2
# Test BZ2Decompressor

with open('data/test.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    with open('data/test.out', 'wb') as out:
        for block in iter(lambda: f.read(100 * 1024), b''):
            out.write(decompressor.decompress(block))
        out.write(decompressor.flush())
# Test BZ2File

with bz2.BZ2File('data/test.bz2', 'rb') as f:
    with open('data/test.out', 'wb') as out:
        for block in iter(lambda: f.read(100 * 1024), b''):
            out.write(block)
# Test BZ2File with context manager

with bz2.BZ2File('data/test.bz2', 'rb') as f:
    with open('data/test.out', 'wb') as out:
        for block in iter(lambda: f.read(100 * 1024), b''):
            out.write
