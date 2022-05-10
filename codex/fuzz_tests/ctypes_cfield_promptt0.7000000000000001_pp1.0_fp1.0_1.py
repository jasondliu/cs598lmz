import ctypes
# Test ctypes.CField.
#

import sys
import unittest
from test import test_support

class X(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_byte),
        ("b", ctypes.c_byte),
        ctypes.CField("c", ctypes.c_byte),
        ("d", ctypes.c_int),
        ]

class Y(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_byte),
        ("b", ctypes.c_byte),
        ("c", ctypes.c_byte),
        ("d", ctypes.c_int),
        ]

class Z(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_byte),
        ("b", ctypes.c_byte),
#        ctypes.CField("c", ctypes.c_byte),
        ("d", ctypes.c_int),
        ]

class T(ctypes.Structure):
    _fields_ = [

