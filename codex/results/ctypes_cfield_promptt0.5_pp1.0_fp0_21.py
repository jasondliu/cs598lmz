import ctypes
# Test ctypes.CField

import _ctypes_test

class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("x", X)]

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("x", ctypes.CField(X))]

# this should not raise an exception
X._fields_ = [("x", ctypes.c_int),
              ("y", ctypes.c_int)]

print X._fields_

# this should not raise an exception
Y._fields_ = [("a", ctypes.c_int),
              ("b", ctypes.c_int),
              ("x", X)]

print Y._fields_

# this should not raise an exception

