import ctypes
# Test ctypes.CFUNCTYPE with PyCFuncPtr_New
def func_pycfuncptr_new(a, b):
    return 2 * (a + b)

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
pyfunc = CMPFUNC(func_pycfuncptr_new)

test_values = [(0, 0),
               (1, 0),
               (0, 1),
               (1, 1),
               (sys.maxint, 0),
               (0, sys.maxint),
               (sys.maxint, sys.maxint),
               (-1, 0),
               (0, -1),
               (-1, 1),
               (1, -1),
               (-1, sys.maxint),
               (sys.maxint, -1),
               ]

def test_pycfuncptr_new():
    for a, b in test_values:
        res = pyfunc(a, b)
        expected = 2 * (a + b)
        if res
