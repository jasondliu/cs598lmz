import bz2
# Test BZ2Decompressor

with open('data/test.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    with open('data/test.txt', 'wb') as fout:
        for block in iter(lambda: f.read(100 * 1024), b''):
            fout.write(decompressor.decompress(block))
        fout.write(decompressor.flush())
 
# Test BZ2Compressor

with open('data/test.txt', 'rb') as fin:
    with bz2.open('data/test.bz2', 'wb') as fout:
        fout.writelines(fin)
 
# Test BZ2File

with bz2.open('data/test.bz2', 'rb') as fin:
    with open('data/test.txt', 'wb') as fout:
        fout.write(fin.read())
 
with open('data/test.txt', 'rb') as fin:
    with bz2.open('data/test.
