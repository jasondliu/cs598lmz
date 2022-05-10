import ctypes
# Test ctypes.CFUNCTYPE()


def test_CFUNCTYPE_0():

    # check that c_byte as ctypes.c_byte*3 returns a pointer to ctypes.c_byte
    c_byte_p = ctypes.c_byte * 3
    assert type(c_byte_p) is ctypes._Pointer

    # check that ctypes.CFUNCTYPE(c_byte) works
    c_byte_p_p = ctypes.CFUNCTYPE(c_byte_p)
    assert type(c_byte_p_p) is ctypes._CFuncPtr

    # check that ctypes.CFUNCTYPE(c_byte) returns a pointer to c_byte
    c_byte_p_p_p = ctypes.CFUNCTYPE(c_byte_p_p)
    assert type(c_byte_p_p_p) is ctypes._CFuncPtr

    # check that ctypes.CFUNCTYPE(c_byte) with 3 args works
    c_byte_p_p_p_p = ctypes.CFUN
