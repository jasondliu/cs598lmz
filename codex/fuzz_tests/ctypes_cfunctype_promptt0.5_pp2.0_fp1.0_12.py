import ctypes
# Test ctypes.CFUNCTYPE

import ctypes
import _ctypes_test

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char_p),
                ("b", ctypes.c_int)]

def func(a, b):
    print(a, b)
    return a + b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, X, X)
f = CMPFUNC(func)

x = X(b"hello", 42)
y = X(b"world", -1)
print(f(x, y))
print(f(y, x))

_ctypes_test.set_callback(CMPFUNC, f)
print(_ctypes_test.call_callback(x, y))
print(_ctypes_test.call_callback(y, x))

# Test CFUNCTYPE with a function that takes a variable number of arguments

def func(*args):
    print(args)
    return len(args)

f = ctypes.CFUN
