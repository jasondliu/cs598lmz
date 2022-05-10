import ctypes
# Test ctypes.CFUNCTYPE

def test_CFUNCTYPE():
    import _ctypes_test
    dll = ctypes.CDLL(_ctypes_test.__file__)
    func = dll._testfunc_p_p
    func.argtypes = (ctypes.c_void_p,)
    func.restype = ctypes.c_void_p

    def callback(x):
        return x

    cb = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)(callback)
    res = func(cb)
    assert res == cb

def test_CFUNCTYPE_errcheck():
    import _ctypes_test
    dll = ctypes.CDLL(_ctypes_test.__file__)
    func = dll._testfunc_p_p
    func.argtypes = (ctypes.c_void_p,)
    func.restype = ctypes.c_void_p

    def callback(x):
        return x

