import ctypes
# Test ctypes.CFUNCTYPE

def func(a, b):
    return a + b

int_func = ctypes.CFUNCTYPE(ctypes.c_int,
                            ctypes.c_int, ctypes.c_int)(func)

assert int_func(1, 2) == 3

try:
    int_func('a', b'b')
except TypeError:
    pass
else:
    raise AssertionError("should have raised")

try:
    int_func(1, 2, 3)
except TypeError:
    pass
else:
    raise AssertionError("should have raised")

# Test ctypes.PYFUNCTYPE

def py_func(a, b):
    return a + b

int_func = ctypes.PYFUNCTYPE(ctypes.c_int,
                             ctypes.c_int, ctypes.c_int)(py_func)

assert int_func(1, 2) == 3
assert int_func('a', 'b') == 'ab'

try:
   
