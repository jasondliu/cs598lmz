import ctypes
# Test ctypes.CFUNCTYPE
def test_CFUNCTYPE():
    print "Test ctypes.CFUNCTYPE"
    import _ctypes_test
    dll = ctypes.CDLL(_ctypes_test.__file__)
    # prototype a function type
    prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
    # get adress of function
    restype = ctypes.c_int
    argtypes = (ctypes.c_int,)
    func = prototype(( "func_type", dll), ((restype, argtypes)))
    # call the function
    print func(42)
    # check the type of the function
    assert isinstance(func, ctypes._CFuncPtr), `type(func)`

# Test ctypes.c_void_p.from_param()
def test_void_p_from_param():
    print "Test ctypes.c_void_p.from_param()"
    class X(object):
        pass
    x = X()
    x.__int__ = lambda
