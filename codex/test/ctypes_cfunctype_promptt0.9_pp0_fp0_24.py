import ctypes
# Test ctypes.CFUNCTYPE()
# XXX this should be in ctypes/test/test_cfunctype.py
import _ctypes_test
from ctypes import *
import unittest

class POINT(Structure):
    _fields_ = [("x", c_int), ("y", c_int)]

def callback(my_func, p1, p2=None, p3=None):
    pt = POINT(1, 0)
    if p3:
        my_func(byref(pt), p1, p2, p3)
    elif p2:
        my_func(byref(pt), p1, p2)
    else:
        my_func(byref(pt), p1)
    return pt.x

callback_f = CFUNCTYPE(None, POINTER(POINT), c_int, c_int, c_int)

tests = {}
class test(object):
    def __init__(self, index):
        self.index = index

