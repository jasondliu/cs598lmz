import ctypes
# Test ctypes.CField.from_address()
# This is not an automatic test suite!
#
# This test program expects to find in the shared library a modest
# variable of type 'int' at address 0xFFFFFFF0 (to test the
# "address" parameter). It also expects to find an array of ints of size
# 6, starting at address 0xFFFFFFC0. The last element of the array is a
# copy of the first variable.

lib = ctypes.CDLL("test")

class X(ctypes.Structure):
    _fields_ = ctypes.CField("a1", ctypes.c_int, 0xFFFFFFC0),\
               ctypes.CField("a2", ctypes.c_int, 0xFFFFFFC4),\
               ctypes.CField("a3", ctypes.c_int, 0xFFFFFFC8),\
               ctypes.CField("a4", ctypes.c_int, 0xFFFFFFCC),\
               ctypes.CField("a5", ctypes.c_int, 0xFFFFFFD0),\
