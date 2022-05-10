import bz2
# Test BZ2Decompressor

def test_bz2_decompressor_2arg_init():
    decompressor = bz2.BZ2Decompressor()
    assert decompressor.unused_data == b''
    assert decompressor.eof == 0

def test_bz2_decompressor_1arg_init(space):
    w_decompressor = space.appexec([], """():
    import bz2
    return bz2.BZ2Decompressor(42)
    """)
    py_decompressor = space.interp_w(W_BZ2Decompressor, w_decompressor)
    assert py_decompressor.unused_data == b'42'
    assert py_decompressor.eof == 0
