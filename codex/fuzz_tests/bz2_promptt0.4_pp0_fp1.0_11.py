import bz2
# Test BZ2Decompressor

with bz2.BZ2File('data/sample.bz2') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100 * decompressor.decompress(f.read(100))), b''):
        print(block)

# Test BZ2Compressor

with bz2.BZ2File('data/sample.bz2', 'w') as f:
    compressor = bz2.BZ2Compressor()
    for data in ['a', 'b', 'c', 'd']:
        f.write(compressor.compress(data))
    f.write(compressor.flush())
 
import bz2
# Test BZ2Decompressor

with bz2.BZ2File('data/sample.bz2') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100 * decompressor.decompress(f.read(100))), b''):
