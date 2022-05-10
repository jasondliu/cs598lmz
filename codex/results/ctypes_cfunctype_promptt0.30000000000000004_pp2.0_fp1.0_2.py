import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
assert cb(1, 2) == 3
# Test ctypes.PYFUNCTYPE
def func(a, b):
    return a + b

cb = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
assert cb(1, 2) == 3
# Test ctypes.WINFUNCTYPE
def func(a, b):
    return a + b

cb = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
assert cb(1, 2) == 3
# Test ctypes.CFUNCTYPE with a class
class Foo:
    def __init__(self):
        self.cb = ctypes.CFUNCTYPE(ctypes.c_int
