import bz2
# Test BZ2Decompressor
with bz2.BZ2File('test.bz2', 'rb') as c:
    decomp = bz2.BZ2Decompressor()
    print(decomp.decompress(c.read()).decode())

# Test BZ2Compressor
comp = bz2.BZ2Compressor()
with bz2.BZ2File('test2.bz2', 'wb') as c:
    for i in range(100):
        c.write(comp.compress(f'{i}\n'.encode()))
    c.write(comp.flush())

# Test BZ2File
with bz2.BZ2File('test3.bz2', 'wt') as c:
    for i in range(100):
        c.write(f'{i}\n')

with bz2.BZ2File('test3.bz2', 'rt') as c:
    print(c.read())
