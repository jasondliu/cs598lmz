import ctypes
# Test ctypes.CFUNCTYPE

def test_cfunctype():
    import _ctypes_test
    dll = ctypes.CDLL(_ctypes_test.__file__)
    func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(("myfunc", dll))
    assert func(5) == 6

def test_cfunctype_call_conv():
    import _ctypes_test
    dll = ctypes.CDLL(_ctypes_test.__file__)
    func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int,
                            call_conv=ctypes.c_int)(("myfunc", dll))
    assert func(5) == 6

def test_cfunctype_restype():
    import _ctypes_test
    dll = ctypes.CDLL(_ctypes_test.__file__)
    func = ctypes.CFUNCTYPE(None, ctypes.c_int)(("myfunc", dll))
