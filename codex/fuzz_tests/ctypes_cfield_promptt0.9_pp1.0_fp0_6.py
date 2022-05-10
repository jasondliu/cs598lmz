import ctypes
# Test ctypes.CField()

from ctypes import *
import sys

if sys.platform == "win32":
        from _ctypes_test import *

c_int_p = POINTER(c_int)
if sys.platform == "win32":
    c_stdcall_p = c_void_p
else:
    c_stdcall_p = c_int
    
class X(Structure):
    _fields_ = [
        ("next", c_int),
        ("callback", c_stdcall_p),
        ("param", c_int_p),
    ]
    _anonymous_ = ["next"]

    def func(self):
        self.param = 42

x = X()
print x.param
x.func()
if x.param != 42:
    raise ValueError("The function did not modify the pointer")
