import _struct
# Test _struct.Struct over longer than 64-bit integers
# to exercise ctypes implementation

import _struct
from _struct import Struct
from ctypes import LittleEndianStructure, BigEndianStructure, \
     Union, c_int64, c_ubyte, c_char, c_int, c_uint

class SLE(LittleEndianStructure):
    _pack_ = 1
    _fields_ = [("x", c_int64)]

class SBE(BigEndianStructure):
    _pack_ = 1
    _fields_ = [("x", c_int64)]

class ULE(LittleEndianStructure):
    _pack_ = 1
    _fields_ = [("x", c_uint)]

class UBE(BigEndianStructure):
    _pack_ = 1
    _fields_ = [("x", c_uint)]

class ULE2(Union):
    _pack_ = 1
    _fields_ = [("x", c_uint),
                ("y", c_ubyte * 4)]

