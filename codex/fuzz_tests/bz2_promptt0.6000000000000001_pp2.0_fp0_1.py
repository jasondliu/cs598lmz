import bz2
# Test BZ2Decompressor.decompress() with a small buffer size
# to test the code path that processes data in multiple chunks.
# This is important because the bz2 module is used to decompress
# log files, which are usually large and therefore must be processed
# in chunks.

# decompress() should return the empty string when no more data is available

decomp = bz2.BZ2Decompressor()
assert decomp.decompress(b'') == b''

# decompress() should raise an exception if the compressed data is truncated

with pytest.raises(IOError):
    decomp.decompress(b'BZh')

# decompress() should return the empty string when the end of the
# compressed data has been reached.

with open(TESTFN, 'wb') as f:
    f.write(bz2.compress(b'x' * 1000))
with open(TESTFN, 'rb') as f:
    data = f.read(500)
    decomp = bz2.BZ2Decompressor()
    x = decomp.decompress
