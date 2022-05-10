import ctypes
# Test ctypes.CFUNCTYPE
def func1(a, b):
    return a + b

type_func1 = type(func1)
