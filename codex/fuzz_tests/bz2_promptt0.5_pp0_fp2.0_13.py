import bz2
# Test BZ2Decompressor.seekable()

with bz2.BZ2File(TESTFN, mode='wb') as f:
    f.write(b'abc')

with bz2.BZ2File(TESTFN, mode='rb') as f:
    d = bz2.BZ2Decompressor()
    assert d.seekable() is False
    assert d.decompress(f.read()) == b'abc'
    assert d.seekable() is False

with bz2.BZ2File(TESTFN, mode='rb') as f:
    d = bz2.BZ2Decompressor()
    f.seek(0)
    assert d.seekable() is False
    assert d.decompress(f.read()) == b'abc'
    assert d.seekable() is False

with bz2.BZ2File(TESTFN, mode='rb') as f:
    d = bz2.BZ2Decompressor()
    f.seek(0)
    assert d.seekable() is False
    assert
