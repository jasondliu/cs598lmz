import ctypes
# Test ctypes.CField.

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

x = X()
x.a = 1
try:
    x.a = "hello"
except TypeError:
    print("TypeError")

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.CField)]

y = Y()
y.a = 1
try:
    y.a = "hello"
except TypeError:
    print("TypeError")
