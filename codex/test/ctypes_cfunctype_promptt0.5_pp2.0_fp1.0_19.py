import ctypes
# Test ctypes.CFUNCTYPE
def test_cfunc():
    # Test ctypes.CFUNCTYPE
    # XXX: Test the rest of the ctypes stuff
    import ctypes
    f1 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(lambda x,y: x+y)
    assert f1(2, 3) == 5
    f2 = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(ctypes.c_int))(lambda x,y: y[0]*x)
    x = ctypes.c_int(2)
    f2(2, x)
    assert x.value == 4
    f3 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)(lambda x: ord(x[0]))
    assert f3(b"a") == 97
