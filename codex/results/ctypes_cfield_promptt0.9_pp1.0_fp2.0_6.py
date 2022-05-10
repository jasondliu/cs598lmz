import ctypes
# Test ctypes.CField.
from ctypes import *

class X(Union):
    _fields_ = [("a", c_int),
                ("b", c_char*4)]

class XS(Structure):
    pass
XS._fields_ = [("s", c_short),
               ("x", X)]

class Test(Structure):
    pass
Test._fields_ = [("a", c_char),
                 ("b", c_char * 4)]

tests = [("a", "c_char"),
         ("b", "*c_char_Array_4"),
         ("a.a", "c_int"),
         ("a.b", "*c_char_Array_4"),
         ("b.a", "c_int"),
         ("b.b", "*c_char_Array_4"),
         ("c.a", "c_int"),
         ("c.b", "*c_char_Array_4")
         ]

for name, type in tests:
    try:
        print name, getattr(Test, name), type(getattr
