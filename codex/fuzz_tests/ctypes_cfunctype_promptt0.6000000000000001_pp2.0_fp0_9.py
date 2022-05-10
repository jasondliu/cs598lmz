import ctypes
# Test ctypes.CFUNCTYPE on a generic function
def func(x, y):
    if x != y:
        raise ValueError
    return x
CFUNCTYPE(c_int, c_int, c_int)(func)
# Test ctypes.CFUNCTYPE on a function that takes a callback
def func2(f, x, y):
    if f(x, y) != x:
        raise ValueError
    return x
CFUNCTYPE(c_int, CFUNCTYPE(c_int, c_int, c_int), c_int, c_int)(func2)
# Test ctypes.CFUNCTYPE on a function that takes a callback
# which takes a callback
def func3(f, x, y):
    if f(x, y) != x:
        raise ValueError
    return x
def func4(f):
    return func3(f, 2, 2)
CFUNCTYPE(c_int, CFUNCTYPE(c_int, c_int, c_int))(func4)
# Test ctypes.CFUN
