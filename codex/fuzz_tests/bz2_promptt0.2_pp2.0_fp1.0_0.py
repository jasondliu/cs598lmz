import bz2
# Test BZ2Decompressor

with open('data/sample.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    with open('data/sample.txt', 'wb') as fout:
        for block in iter(lambda: f.read(100 * 1024), b''):
            fout.write(decompressor.decompress(block))
        fout.write(decompressor.flush())
 
# Test BZ2Compressor

with open('data/sample.txt', 'rb') as f:
    compressor = bz2.BZ2Compressor()
    with open('data/sample.bz2', 'wb') as fout:
        for block in iter(lambda: f.read(100 * 1024), b''):
            fout.write(compressor.compress(block))
        fout.write(compressor.flush())
 
# Test BZ2File

with bz2.BZ2File('data/sample.bz2', 'rb') as fin:
    with open('data/sample.txt
