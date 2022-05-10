import ctypes
# Test ctypes.CFUNCTYPE

import ctypes
from ctypes import *

def func(*args):
    return args

FUNC = CFUNCTYPE(c_int, c_int, c_int, c_int)

f = FUNC(func)

print f(1, 2, 3)

# Test ctypes.POINTER(<type>)

import ctypes
from ctypes import *

class Bar(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int)]

class Foo(Structure):
    _fields_ = [("bar", POINTER(Bar))]

foo = Foo()
foo.bar = pointer(Bar(1, 2))

print foo.bar.contents.a
print foo.bar.contents.b

# Test ctypes.wintypes

import ctypes
from ctypes import *

print wintypes.BOOL
print wintypes.BYTE
print wintypes.CHAR
print wintypes.DWORD
print wintypes.HANDLE
print wintypes
