import ctypes
# Test ctypes.CFUNCTYPE() and ctypes.PYFUNCTYPE()
# The function types are the same:
assert ctypes.CFUNCTYPE(ctypes.c_int) == ctypes.PYFUNCTYPE(ctypes.c_int)
assert ctypes.CFUNCTYPE(None) == ctypes.PYFUNCTYPE(None)
# POINTER(CFUNCTYPE) != POINTER(PYFUNCTYPE), though
assert ctypes.POINTER(ctypes.CFUNCTYPE(ctypes.c_int)) != ctypes.POINTER(ctypes.PYFUNCTYPE(ctypes.c_int))
assert ctypes.POINTER(ctypes.CFUNCTYPE(None)) != ctypes.POINTER(ctypes.PYFUNCTYPE(None))
# But a CFUNCTYPE() can be passed to a function expecting a PYFUNCTYPE()
def f(func):
    return func(3)
assert f(ctypes.CFUNCTYPE(ctypes.c_int)(lambda x: x*
