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
assert f(1) == 1

f = ctypes.PYFUNCTYPE(ctypes.c_int)(func)
assert f(2) == 2

# Test ctypes.CFUNCTYPE/ctypes.PYFUNCTYPE with (int) -> (void)
def func(a):
    print(a)

f = ctypes.CFUNCTYPE(None, ctypes.c_int)(func)
f(3)

f = ctypes.PYFUNCTYPE
