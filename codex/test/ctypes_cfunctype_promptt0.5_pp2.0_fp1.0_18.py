import ctypes
# Test ctypes.CFUNCTYPE()

def func(x):
    print(x)

cfunc = ctypes.CFUNCTYPE(None, ctypes.c_int)(func)
cfunc(3)

# Test ctypes.WINFUNCTYPE()

def func(x):
    print(x)

