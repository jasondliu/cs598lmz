import bz2
# Test BZ2Decompressor with a file containing an empty stream.

data = bz2.BZ2Compressor().compress(b'')
assert bz2.decompress(data) == b''

with open(TESTFN, 'wb') as f:
    f.write(data)
with bz2.open(TESTFN, 'rb') as f:
    assert f.read() == b''

with open(TESTFN, 'wb') as f:
    f.write(data)
with bz2.open(TESTFN, 'rt') as f:
    assert f.read() == ''

with open(TESTFN, 'wb') as f:
    f.write(data)
with bz2.open(TESTFN, 'rt', encoding='latin-1') as f:
    assert f.read() == ''

with open(TESTFN, 'wb') as f:
    f.write(data)
with bz2.open(TESTFN, 'rt', encoding='utf-8') as f:
    assert f.read() ==
