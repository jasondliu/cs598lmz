import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("one", ctypes.c_uint), ("two", ctypes.c_uint)]
    _anonymous_ = ("one",)

x = ctypes.cast(b"Z\0\0\0\0\0\0\0", ctypes.POINTER(X))
print(x.contents.two)

# Test ctypes.CArray
class Y(ctypes.Structure):
    _fields_ = [("ints", ctypes.c_int * 4)]
s = Y()
print(list(s.ints))
s.ints[2] = 3
print(list(s.ints))

# Test ctypes.CFixedArray
class Z(ctypes.Structure):
    _fields_ = [("fixed", ctypes.c_byte * 4)]
t = Z()
t.fixed[1] = 2
print(list(t.fixed))

def run_tests():
    import re
    import sys
    import os
    open("ctypes_types.txt", "
