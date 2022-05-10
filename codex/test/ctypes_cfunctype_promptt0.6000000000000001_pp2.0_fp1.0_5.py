import ctypes
# Test ctypes.CFUNCTYPE/ctypes.PYFUNCTYPE with (void) -> (void)
def func():
    print("in func")

f = ctypes.CFUNCTYPE(None)(func)
f()

f = ctypes.PYFUNCTYPE(None)(func)
f()

# Test ctypes.CFUNCTYPE/ctypes.PYFUNCTYPE with (int) -> (int)
def func(a):
    return a

f = ctypes.CFUNCTYPE(ctypes.c_int)(func)
