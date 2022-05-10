import ctypes
# Test ctypes.CFUNCTYPE(None)

def func(x):
    print x

type_ = ctypes.CFUNCTYPE(None)
f = type_(func)
f(42)

# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(a):
    return a * 2

type_ = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
f = type_(func)
assert f(5) == 10
