import ctypes
# Test ctypes.CFUNCTYPE()

def func(x):
    print(x)

cfunc = ctypes.CFUNCTYPE(None, ctypes.c_int)(func)
cfunc(3)

# Test ctypes.WINFUNCTYPE()

def func(x):
    print(x)

cfunc = ctypes.WINFUNCTYPE(None, ctypes.c_int)(func)
cfunc(3)

# Test ctypes.PYFUNCTYPE()

def func(x):
    print(x)

cfunc = ctypes.PYFUNCTYPE(None, ctypes.c_int)(func)
cfunc(3)

# Test ctypes.CFUNCTYPE() with a tuple

def func(x, y):
    print(x + y)

cfunc = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)(func)
cfunc(3, 4)

# Test ctypes.WINFUNCTYPE() with a tuple

def func(
