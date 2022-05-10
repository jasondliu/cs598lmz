import bz2
# Test BZ2Decompressor object
with bz2.open('test.bz2', 'rb') as fin, open('test', 'wb') as fout:
    decom = bz2.BZ2Decompressor()
    data = fin.read(10000)
