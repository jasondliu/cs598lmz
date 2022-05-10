import ctypes
# Test ctypes.CField: large field, not last field
from ctypes import *

class X(Structure):
    _fields_ = [("a", c_int64),
                ("b", c_byte*0x80000)]

class Y(Structure):
    _fields_ = [("a", c_byte),
                ("b", X)]

    def set(self):
        self.a = ord('x')
        self.b.a=0
        for i in range(0x80000):
            self.b.b[i] = chr(ord('0') + i)

x = Y()
x.set()
p = pointer(x)

import _ctypes
print p.contents.a
print p.contents.b.a
print p.contents.b.b[42]
print p.contents.b.b[0x80000-1]

import ctypes
assert ctypes.sizeof(x) == 80000
