import ctypes
# Test ctypes.CFUNCTYPE.
def test_CFUNCTYPE():
    from ctypes import CFUNCTYPE, c_int
    c_call_int = CFUNCTYPE(c_int, c_int, c_int)
    lib = ctypes.CDLL(ctypes.util.find_library("c"))
    powi = lib.pow
    powi.argtypes = (c_int, c_int)
    powi.restype = c_int
    a = c_call_int(powi)
    assert a(2, 3) == 8
    #
    try:
        CFUNCTYPE(c_int, c_int, c_int, c_int)
    except ValueError:
        pass
    else:
        raise Exception("should have raised")
    try:
        c_call_int = CFUNCTYPE(c_int, c_int, c_int, c_int)
    except TypeError:
        pass
    else:
        raise Exception("should have raised")
    #
