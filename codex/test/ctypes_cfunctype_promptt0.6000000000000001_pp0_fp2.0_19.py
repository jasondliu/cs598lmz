import ctypes
# Test ctypes.CFUNCTYPE
def foo(x, y):
    return x - y

cb_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
cb = cb_type(foo)

assert cb(1, 2) == -1
# Test ctypes._CFuncPtr
def foo(x, y):
    return x - y

