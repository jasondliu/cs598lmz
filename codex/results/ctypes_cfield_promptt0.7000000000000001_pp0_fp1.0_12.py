import ctypes
# Test ctypes.CField

# This test is for a C compiler that does not support anonymous unions.
# (gcc does support them, and the test for them is in test_anonymous.py)
#
# The following C code is compiled, and the resulting DLL is tested:
#
# typedef struct {
#   int a;
#   union {
#     int b;
#     int c;
#   } u;
#   int d;
# } A;
#
# A *get_A(void) {
#   static A x;
#   x.a = 42;
#   x.u.b = 24;
#   x.d = 88;
#   return &x;
# }

from ctypes import *

class U(Union):
    _fields_ = [("b", c_int),
                ("c", c_int)]

class A(Structure):
    _fields_ = [("a", c_int),
                ("u", U),
                ("d", c_int)]

dll = CDLL(ctypes.util.find_library
