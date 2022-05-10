import bz2
# Test BZ2Decompressor

with bz2.BZ2File('data/sample.bz2') as src, open('data/sample.txt', 'wt') as dst:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: src.read(100 * decompressor.decompress_block.__defaults__[0]), b''):
        dst.write(decompressor.decompress(block))

# Test BZ2Compressor

with open('data/sample.txt', 'rt') as src, bz2.BZ2File('data/sample.bz2', 'wb') as dst:
    compressor = bz2.BZ2Compressor()
    for block in iter(lambda: src.read(100), b''):
        dst.write(compressor.compress(block))
    dst.write(compressor.flush())
 
# Test BZ2File

with bz2.BZ2File('data/sample.bz2') as src, open('data/sample.txt', 'wt') as dst:

