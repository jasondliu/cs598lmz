import ctypes
# Test ctypes.CField and ctypes._CDataMeta

from ctypes import *

TD3 = "a3b"
TD6 = "ccb"
TD8 = "dccb"
TD9 = "bccb"
TD10 = "abcbcb"
TD12 = "?abcbcb"
TD15 = "b?abcbcb"
TD17 = "c?abcbcb"

class Test2(Structure):
    _fields_ = [("c_char", c_char)]

TD2 = "b"

class Test3(Structure):
    _fields_ = [("a", c_char),
                ("b", c_char),
                ("c", c_char)]

class Test4(Structure):
    _fields_ = [("c_int", c_int)]

TD4 = "i"

class Test5(Structure):
    _fields_ = [("c_int", c_int),
                ("c_int", c_int)]

TD5 = "ii"

class Test6(Structure):
    _fields_
