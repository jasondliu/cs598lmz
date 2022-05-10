import ctypes
# Test ctypes.CFUNCTYPE

def test_cfunctype():
    # check the type of function returned by ctypes.CFUNCTYPE
    from ctypes import c_int, c_double, c_char_p, CFUNCTYPE
    f = CFUNCTYPE(c_int, c_double, c_char_p)(lambda x, y: 0)
    assert isinstance(f, CFUNCTYPE(c_int, c_double, c_char_p))
    # check the type of the 'restype' attribute
    assert f.restype is c_int
    # check the type of the 'argtypes' attribute
    assert f.argtypes == (c_double, c_char_p)
    # check that the 'errcheck' attribute is None
    assert f.errcheck is None
    # check that the 'argtypes' attribute is read-only
    raises(TypeError, "f.argtypes = (c_int, c_int)")
    # check that the 'errcheck' attribute is read-only
