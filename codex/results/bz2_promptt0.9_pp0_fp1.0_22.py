import bz2
# Test BZ2Decompressor.seekable()
assert bz2.BZ2Decompressor().seekable() == False
# Hypothesis: the documentation should reflect current behaviour
help(bz2.compress) == help(bz2.BZ2Compressor)
help(bz2.decompress) == help(bz2.BZ2Decompressor)
# Test exception raised when bz2.compress() is passed less than 9 bytes
with pytest.raises(ValueError) as excinfo:
    bz2.compress(b'12345678')
assert str(excinfo.value) == 'at least 9 bytes are needed'

with pytest.raises(ValueError) as excinfo:
    bz2.compress(b'123456789', 1)
assert str(excinfo.value) == 'at least 9 bytes are needed, got 9'

# At least 9 bytes are needed because the bz2lib doesn't accept less
# than 9 bytes for compression. The bz2lib is a C implementation from
# the bzip2 project adapted to Python.

inner_
