import ctypes
# Test ctypes.CFUNCTYPE
def func1(a, b):
    return a + b

type_func1 = type(func1)
assert type_func1 is ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Test ctypes.WINFUNCTYPE
def func2(a, b):
    return a + b

type_func2 = type(func2)
assert type_func2 is ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
