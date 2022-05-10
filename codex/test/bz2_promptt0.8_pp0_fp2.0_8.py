import bz2
# Test BZ2Decompressor
with bz2.BZ2File('test.bz2', 'rb') as c:
    decomp = bz2.BZ2Decompressor()
