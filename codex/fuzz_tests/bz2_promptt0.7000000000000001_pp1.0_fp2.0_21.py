import bz2
# Test BZ2Decompressor.eof
with bz2.BZ2File(TESTFN, 'wb') as f:
    f.write(b'x' * 100000)
with bz2.BZ2File(TESTFN) as f:
    decomp = f.decompressor
    for x in range(10):
        decomp.eof
with bz2.BZ2File(TESTFN) as f:
    decomp = f.decompressor
    f.read(1)
    decomp.eof
with bz2.BZ2File(TESTFN) as f:
    decomp = f.decompressor
    for x in range(10):
        decomp.eof
# Test BZ2Decompressor.unused_data
with bz2.BZ2File(TESTFN, 'wb') as f:
    f.write(b'x' * 100000)
with bz2.BZ2File(TESTFN) as f:
    decomp = f.decompressor
    for x in range(10):
        unused = decomp.unused
