import ctypes
# Test ctypes.CField.from_address
#
# This test is based on the following code:
#
#   from ctypes import *
#   class X(Structure):
#       _fields_ = [("a", c_int),
#                   ("b", c_int)]
#
#   x = X()
#   x.a = 42
#   x.b = 17
#
#   print X.a.from_address(addressof(x))
#   print X.b.from_address(addressof(x))
#
#   print X.a.from_address(addressof(x) + 4)
#   print X.b.from_address(addressof(x) + 4)

import ctypes

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

x = X()
x.a = 42
x.b = 17

print(X.a.from_address(ctypes.addressof(x)))
print(X
