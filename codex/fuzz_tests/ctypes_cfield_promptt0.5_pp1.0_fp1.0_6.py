import ctypes
# Test ctypes.CField.from_address()

from ctypes import *

class X(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int),
                ("c", c_int)]

class Y(Structure):
    _fields_ = [("x", X),
                ("d", c_int)]

class Z(Structure):
    _fields_ = [("y", Y),
                ("e", c_int)]

z = Z()
z.y.x.a = 1
z.y.x.b = 2
z.y.x.c = 3
z.y.d = 4
z.e = 5

print(z.y.x.a, z.y.x.b, z.y.x.c, z.y.d, z.e)

# from the address of x.a, create a field object
f = c_int.from_address(addressof(z.y.x.a))

# change the value of x.a
f.value = 42

# all
