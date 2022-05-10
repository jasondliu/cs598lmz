import ctypes
# Test ctypes.CFUNCTYPE()

import ctypes

def func(arg):
    print "hello", arg
    return arg

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)
print cmp_func(42)

# Test ctypes.POINTER()

import ctypes

class Bar(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

class Foo(ctypes.Structure):
    _fields_ = [("bar", Bar)]

f = Foo()
f.bar.a = 42
f.bar.b = 24

print f.bar.a, f.bar.b

# Test ctypes.byref()

import ctypes

class Bar(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

class Foo(ctypes.Structure):
    _
