import ctypes
# Test ctypes.CField instance
import array
import sys
import gc
import unittest
from test import test_support

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_byte),
                ("b", ctypes.c_byte),
                ("dummy", ctypes.c_byte * 2),
                ("c", ctypes.c_byte)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_byte),
                ("b", ctypes.c_byte),
                ("dummy", ctypes.c_byte * 2),
                ("c", ctypes.c_byte),
                ("d", ctypes.c_byte)]

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_byte),
                ("b", ctypes.c_byte),
                ("dummy", ctypes.c_byte * 2),
                ("c", ctypes.c_byte),
                ("d", ctypes.c_byte),
                ("e", ctypes.
