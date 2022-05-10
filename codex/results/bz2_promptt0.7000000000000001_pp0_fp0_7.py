import bz2
# Test BZ2Decompressor's statefulness

def test_simple():
    d = bz2.BZ2Decompressor()
    assert d.decompress(bz2.compress(b"foo")) == b"foo"
    pytest.raises(EOFError, d.decompress, b"")
