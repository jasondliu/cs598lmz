import ctypes
# Test ctypes.CFUNCTYPE() and ctypes.PYFUNCTYPE()
# by calling functions through the CFUNCTYPE / PYFUNCTYPE
# wrappers.
#
# We pass the return value of CFUNCTYPE and PYFUNCTYPE
# to the function through vtable ptr, and return it

def test_cfunctype(lib):
    c_add = lib.add_function
    c_add.argtypes = (ctypes.c_double, ctypes.c_double)
    c_add.restype = ctypes.c_double
    def add(x, y):
        return x + y

    def test(funcptr, expected):
        print(lib.add_caller(funcptr, 1.0, 2.0), expected)

    test(c_add, add(1.0, 2.0))
    test(ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)(add), add(1.0, 2.0))
    test(ctypes.CFUN
