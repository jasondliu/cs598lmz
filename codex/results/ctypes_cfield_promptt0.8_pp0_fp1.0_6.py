import ctypes
# Test ctypes.CField, ctypes.PYFUNCTYPE, ctypes.CFUNCTYPE, ctypes.py_object

from ctypes import *

F_OK = 0
import os
if os.access("_ctypes_test.dll", F_OK):
    dll = CDLL("_ctypes_test.dll")
    dll._testfunc_p_p.restype = py_object

class Test1(Structure):
    _fields_ = [("a", c_int),
                ("b", c_float)]
    def __init__(self):
        self.a = 0x10101010
        self.b = 0.125

class Test2(Structure):
    _fields_ = [("rec1", Test1),
                ("rec2", Test1)]

class Test3(Structure):
    _fields_ = [("arr", c_int * 2)]

class Test4(Structure):
    _fields_ = [("a", c_int),
                ("b", c_float),
                ("c", POINTER(Test1))
