import bz2
# Test BZ2Decompressor.__repr__()
with bz2.BZ2Decompressor() as f2:
    assert f2.__repr__() == object.__repr__(f2)
