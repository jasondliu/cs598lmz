import ctypes
# Test ctypes.CFUNCTYPE()

import ctypes

def func(a, b):
    return a * b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)

print(cmp_func(2, 3))

# Test ctypes.Structure()

import ctypes

class Bar(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

bar = Bar(1, 2)
print(bar.a, bar.b)

# Test ctypes.POINTER()

import ctypes

class Bar(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

bar = Bar(1, 2)
bar_pointer = ctypes.POINTER(Bar)(bar)
print(bar_pointer.contents.a, bar_pointer.
