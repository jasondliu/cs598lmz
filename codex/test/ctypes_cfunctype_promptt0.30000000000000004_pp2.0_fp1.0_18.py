import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import *

def func(x):
    return x

CFunc = CFUNCTYPE(c_int, c_int)

f = func(2)
print(f)

cf = CFunc(func)
print(cf(2))

# Test ctypes.POINTER
from ctypes import *

class POINT(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int)]

pt = POINT(1, 2)
p = pointer(pt)
print(p.contents.x, p.contents.y)

# Test ctypes.c_char_p
from ctypes import *

s = b"Hello, World"
print(c_char_p(s).value)

# Test ctypes.c_wchar_p
from ctypes import *

s = "Hello, World"
print(c_wchar_p(s).value)

# Test ctypes.c_void_p
from ctypes import *

