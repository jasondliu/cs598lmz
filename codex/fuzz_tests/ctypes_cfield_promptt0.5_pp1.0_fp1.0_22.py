import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char_p),
                ("b", ctypes.CField)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char_p),
                ("b", ctypes.CField)]

x = X()
y = Y()

print x.a, x.b
print y.a, y.b

x.a = "hello"
y.a = "world"

print x.a, x.b
print y.a, y.b

x.b = "hello"
y.b = "world"

print x.a, x.b
print y.a, y.b

import _ctypes_test
_ctypes_test.set_cfield(x, "hello")
_ctypes_test.set_cfield(y, "world")

print x.a, x.b
print y.a, y.b

try:
    x.a = "
