import ctypes
# Test ctypes.CField, and add test cases for other types
import unittest, sys
from test import support

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char),
                ("b", ctypes.c_int)]
#    _anonymous_ = ["bar"]

class Y(X):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class Z(ctypes.Union):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_char * 2)]

class ArrayInStruct(ctypes.Structure):
    _fields_ = [("two", ctypes.c_int * 2),
                ("three", ctypes.c_int * 3)]

class ArrayInArray(ctypes.Structure):
    _fields_ = [("array", ctypes.c_int * 2 * 3)]

class ArrayStruct(ctypes.Structure):
    _fields_ = [("length", ctypes.c_int
