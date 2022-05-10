import ctypes
# Test ctypes.CFUNCTYPE and C backend

import ctypes
import _ctypes
from ctypes import _endian
import unittest, sys

LittleEndianStructure = None
BigEndianStructure = None

# For now, we only support LE and BE

if _endian.endian == _endian.LITTLE:
    LittleEndianStructure = ctypes.Structure
    SwapUnion = ctypes.Union
    class BigEndianStructure(ctypes.Structure):
        _swap_ = True
        _fields_ = []
elif _endian.endian == _endian.BIG:
    BigEndianStructure = ctypes.Structure
    SwapUnion = ctypes.Union
    class LittleEndianStructure(ctypes.Structure):
        _swap_ = True
        _fields_ = []

class ArrayTestCase(unittest.TestCase):
    def test_3d_array(self):
        # structure:
        #  short[3][4][5]
        #  int[4]
        #  char
        class
