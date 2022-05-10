import ctypes
# Test ctypes.CFUNCTYPE

# Test a simple function pointer

import ctypes

def func(a, b):
    return a * b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

f = CMPFUNC(func)
print f(2, 3)

# Test a function pointer with unicode and string arguments

import ctypes

def func(a, b):
    return b[::-1] + a

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_char_p, ctypes.c_char_p, ctypes.c_wchar_p)

f = CMPFUNC(func)
print f("hello", u"world")

# Test a function pointer with a struct argument

import ctypes

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

def func(a, b):
   
