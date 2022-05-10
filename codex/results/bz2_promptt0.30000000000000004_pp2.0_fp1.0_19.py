import bz2
# Test BZ2Decompressor

def test_bz2decompressor():
    c = bz2.BZ2Decompressor()
    eq = c.decompress(bz2.compress(b"foo"))
    assert eq == b"foo"
    raises(EOFError, c.decompress, b"")
    raises(EOFError, c.decompress, b"foo")
    raises(EOFError, c.decompress, b"foo", 1)
    raises(EOFError, c.decompress, b"foo", 1, 1)
    raises(EOFError, c.decompress, b"foo", 1, 1, 1)
    raises(EOFError, c.decompress, b"foo", 1, 1, 1, 1)
    raises(EOFError, c.decompress, b"foo", 1, 1, 1, 1, 1)
    raises(EOFError, c.decompress, b"foo", 1, 1, 1, 1, 1, 1)
    raises(EOFError, c.decompress,
