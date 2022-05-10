import ctypes
# Test ctypes.CFUNCTYPE with a simple function

def func(x):
    return x

f = ctypes.CFUNCTYPE(ctypes.c_int)(func)

if f(42) != 42:
    raise Exception("CFUNCTYPE failed")
# Test ctypes.CFUNCTYPE with a function that takes a pointer

def func(x):
    return x[0]

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))(func)

if f([42]) != 42:
    raise Exception("CFUNCTYPE failed")
# Test ctypes.CFUNCTYPE with a function that takes a pointer

def func(x):
    return x.contents.value

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))(func)

if f(ctypes.pointer(ctypes.c_int(42))) != 42:
    raise Exception("CFUNCTYPE failed")
#
