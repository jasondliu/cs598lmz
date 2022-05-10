import ctypes
# Test ctypes.CFUNCTYPE

def test_cfunctype():
    import _ctypes_test
    dll = ctypes.CDLL(_ctypes_test.__file__)
    func = dll._testfunc_p_p
    func.restype = ctypes.c_void_p
    func.argtypes = (ctypes.c_void_p,)

    class X(ctypes.Structure):
        _fields_ = [("x", ctypes.c_int)]

    x = X(1)
    assert func(ctypes.byref(x)) == ctypes.addressof(x)

    #
    # Test that a CFUNCTYPE function can be passed to a function
    # expecting a pointer to a simple function.
    #
    func = dll._testfunc_p_p
    func.restype = ctypes.c_void_p
    func.argtypes = (ctypes.c_void_p,)

    CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
    def callback(
