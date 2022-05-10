import ctypes
# Test ctypes.CFUNCTYPE

def test_cfunctype():
    #
    # Test calling a C function with a simple prototype
    #
    prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
    paramflags = (1, "x", 0),
    restype = ctypes.c_int
    check_type(prototype, paramflags, restype)
    #
    # Test calling a C function with a prototype that uses pointers
    #
    prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))
    paramflags = (1, "x", 0),
    restype = ctypes.c_int
    check_type(prototype, paramflags, restype)
    #
    # Test calling a C function with a prototype that uses pointers to pointers
    #
    prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_int)))
