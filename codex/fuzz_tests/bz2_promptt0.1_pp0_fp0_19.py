import bz2
# Test BZ2Decompressor

with bz2.BZ2File('data/test.bz2', 'r') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100 * 1024), b''):
        data = decompressor.decompress(block)
        if data:
            print(data)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()
with open('data/test.bz2', 'wb') as f:
    for data in ['a', 'b', 'c']:
        f.write(compressor.compress(data))
    f.write(compressor.flush())
 
# Test BZ2File

with bz2.BZ2File('data/test.bz2', 'r') as f:
    print(f.read())

with bz2.BZ2File('data/test.bz2', 'rb') as f:
    print(f.read())

with bz2.BZ2File
