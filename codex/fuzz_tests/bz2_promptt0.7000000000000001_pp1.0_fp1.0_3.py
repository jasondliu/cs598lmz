import bz2
# Test BZ2Decompressor

def test_decompressor_basics():
    c = bz2.BZ2Decompressor()
    eq(c.unused_data, b(''))

    raises(EOFError, c.decompress, b(''))
    raises(EOFError, c.decompress, b('a'))
    raises(EOFError, c.decompress, b('a'*1000))

    eq(c.unconsumed_tail, b(''))
    eq(c.decompress(b('BZh91AY&SY')), b('hello'))
    eq(c.unused_data, b(''))
    eq(c.unconsumed_tail, b(''))

    raises(EOFError, c.decompress, b(''))
    eq(c.unconsumed_tail, b(''))
    raises(EOFError, c.decompress, b('a'))
    eq(c.unconsumed_tail, b('a'))
    raises(EOFError, c.decompress
