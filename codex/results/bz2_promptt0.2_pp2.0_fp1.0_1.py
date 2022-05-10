import bz2
# Test BZ2Decompressor

with open('data/sample.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    with open('data/sample.txt', 'wb') as g:
        for block in iter(lambda: f.read(100 * 1024), b''):
            g.write(decompressor.decompress(block))
        g.write(decompressor.flush())
# Test BZ2File

with bz2.BZ2File('data/sample.bz2', 'rb') as f:
    with open('data/sample.txt', 'wb') as g:
        for block in iter(lambda: f.read(100 * 1024), b''):
            g.write(block)
 
# Test BZ2File with context manager

with bz2.BZ2File('data/sample.bz2', 'rb') as f:
    with open('data/sample.txt', 'wb') as g:
        g.write(f.read())
 
# Test BZ2File with context manager and
