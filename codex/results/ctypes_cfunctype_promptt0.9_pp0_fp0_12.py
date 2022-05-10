import ctypes
# Test ctypes.CFUNCTYPE()
# This could cause a segfault, bug #1477
CFUNCTYPE = ctypes.CFUNCTYPE


def test(lib):
    if lib is not None:
        i = ctypes.c_int()
        f = CFUNCTYPE(None, ctypes.POINTER(ctypes.c_int))(lambda p: None)
        f(i)
        del f
        del i


def test_callback(lib):
    if lib is None:
        return True
    # FT2Font tests
    ffi = ctypes.CDLL(lib)

    # Test ctypes.CFUNCTYPE()
    cfunction = CFUNCTYPE(None, ctypes.POINTER(ctypes.c_int))
    assert cfunction
    assert cfunction.argtypes == (ctypes.POINTER(ctypes.c_int),)
    assert cfunction.restype == None

    # Test that callback functions can be created, passed as arguments,
    # set as attributes, and destroyed
    ffi_callbacks = []

   
