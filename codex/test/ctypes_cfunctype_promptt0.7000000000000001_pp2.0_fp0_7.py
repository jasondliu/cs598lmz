import ctypes
# Test ctypes.CFUNCTYPE with PyCFuncPtr_New
def func_pycfuncptr_new(a, b):
    return 2 * (a + b)

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
pyfunc = CMPFUNC(func_pycfuncptr_new)

