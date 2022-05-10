import ctypes
# Test ctypes.CFUNCTYPE and structs

import ctypes
from ctypes import wintypes
import unittest

class StructsTestCase(unittest.TestCase):
    # Structure/Union classes must be defined first, otherwise the
    # convertion of Structure/Union fields into ctypes instances
    # will fail.
    class Point(ctypes.Structure):
        _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]
        def __init__(self, x=0, y=0):
            super(StructsTestCase.Point, self).__init__(x, y)

    class Line(ctypes.Structure):
        _fields_ = [("begin", Point), ("end", Point)]

    class Color(ctypes.Structure):
        _fields_ = [("red", ctypes.c_ubyte),
                    ("green", ctypes.c_ubyte),
                    ("blue", ctypes.c_ubyte)]

    class UnionTest(ctypes.Union):
        _fields_ = [("color", Color),
