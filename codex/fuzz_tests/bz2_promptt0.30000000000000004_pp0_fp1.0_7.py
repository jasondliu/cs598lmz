import bz2
# Test BZ2Decompressor

with bz2.BZ2File('data/test.bz2') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100 * decompressor.decompress_block.__sizeof__()), b''):
        print(decompressor.decompress(block))

# Test BZ2Compressor

with bz2.BZ2File('data/test.bz2', 'w') as f:
    compressor = bz2.BZ2Compressor()
    f.write(compressor.compress(b'Hello World'))
    f.write(compressor.flush())
 
# Test BZ2File

with bz2.BZ2File('data/test.bz2') as f:
    print(f.read())
 
with bz2.BZ2File('data/test.bz2', 'w') as f:
    f.write(b'Hello World')

# Test compress()

print(bz2.
