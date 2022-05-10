import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def test_CFUNCTYPE():
    # test with a function that takes no arguments
    func = ctypes.CFUNCTYPE(ctypes.c_int)()
    func.restype = ctypes.c_int
    func.argtypes = None
    func.__call__.restype = ctypes.c_int
    func.__call__.argtypes = None

    # test with a function that takes one argument
    func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)()
    func.restype = ctypes.c_int
    func.argtypes = [ctypes.c_int]
    func.__call__.restype = ctypes.c_int
    func.__call__.argtypes = [ctypes.c_int]

    # test with a function that takes two arguments
    func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)()
    func.restype = c
