import bz2
# Test BZ2Decompressor

with bz2.BZ2File('data/test.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100 * 1024), b''):
        data = decompressor.decompress(block)
        print(data)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()
with bz2.BZ2File('data/test.bz2', 'wb') as f:
    for data in ['a', 'b', 'c']:
        f.write(compressor.compress(data))
    f.write(compressor.flush())
 
# Test compress() and decompress()

data = bz2.compress(b'Hello World')
print(data)
print(bz2.decompress(data))
 
# Test compresslevel

data = bz2.compress(b'Hello World', compresslevel=9)
print(data)
print(bz2.dec
