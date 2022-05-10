import bz2
# Test BZ2Decompressor object methods

decomp = bz2.BZ2Decompressor()

def test_bits_read():
    decomp = bz2.BZ2Decompressor()
    assert decomp.decompress(b'x\234\355W\275S\024\004F\006\001\0008') == b'foo'
    assert decomp.decompress(b'') == b''
    assert decomp.decompress(b'') == b''
    assert decomp.unused_data == b''
    assert decomp.eof == False

    # already finished
    raises(EOFError, decomp.decompress, b'x')

    # trigger EOF
    decomp = bz2.BZ2Decompressor()
    raises(EOFError, decomp.decompress, b'x\234\355W\275S\024\004F\006\001\000')
    assert decomp.eof == True
    decomp.reset()
    assert decomp.eof == False
    decomp = bz2.BZ2Decompressor()
