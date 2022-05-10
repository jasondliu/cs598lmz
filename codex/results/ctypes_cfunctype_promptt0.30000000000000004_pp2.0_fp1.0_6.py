import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(a, b):
    return a + b

FuncType = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

f = FuncType(func)
print(f(1, 2))

# Test ctypes.POINTER

import ctypes

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

pt = POINT(1, 2)
p = ctypes.pointer(pt)

print(p.contents)

# Test ctypes.byref

import ctypes

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

pt = POINT(1, 2)

def func(p):
    print(p.contents)

func(ctypes.byref(pt))

