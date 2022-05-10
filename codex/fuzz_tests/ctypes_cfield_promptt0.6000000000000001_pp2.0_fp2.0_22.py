import ctypes
# Test ctypes.CField
from ctypes import *
from ctypes.test import need_symbol

import _ctypes_test

class X(Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c_int),
        ('c', ctypes.c_int),
        ('d', ctypes.c_int),
        ('e', ctypes.c_int),
        ('f', ctypes.c_int),
        ('g', ctypes.c_int),
    ]

class Y(Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c_int),
        ('c', ctypes.c_int),
        ('d', ctypes.c_int),
        ('e', ctypes.c_int),
        ('f', ctypes.c_int),
        ('g', ctypes.c_int),
        ('h', ctypes.c_int),
        ('i', ctypes.c_int),
        ('j', c
