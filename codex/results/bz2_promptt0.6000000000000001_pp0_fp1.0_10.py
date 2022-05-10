import bz2
# Test BZ2Decompressor

with bz2.BZ2File('data/data.bz2', 'rb') as source, open('data/data.txt', 'wb') as target:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda : source.read(1024), b''):
        target.write(decompressor.decompress(block))

# Test BZ2Compressor

with open('data/data.txt', 'rb') as source, bz2.BZ2File('data/data.bz2', 'wb') as target:
    compressor = bz2.BZ2Compressor()
    for block in iter(lambda : source.read(1024), b''):
        target.write(compressor.compress(block))
    target.write(compressor.flush())
 
# Test BZ2File

with bz2.BZ2File('data/data.bz2', 'rb') as source, open('data/data.txt', 'wb') as target:
    for block in iter(lambda : source.
