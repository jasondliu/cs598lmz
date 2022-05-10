import bz2
# Test BZ2Decompressor
c = BZ2Decompressor()
with open(test_file1, 'rb') as f:
    d = c.decompress(f.read())
assert d == b"xxx" + b"\n"
# Test BZ2File
with BZ2File(test_file1) as f:
    assert f.read() == b"xxx" + b"\n"
# Test bz2.compress()
assert bz2.compress(b"xxx") == bz2.compress(b"xxx")[:10]
# Test bz2.decompress()
assert bz2.decompress(bz2.compress(b"xxx")) == b"xxx"
# Test bz2.open()
with bz2.open(test_file1, mode='rt') as f:
    assert f.read() == "xxx" + "\n"
# Test bz2.BZ2File
with bz2.BZ2File(test_file1) as f:
    assert f.read() == b"xxx" +
