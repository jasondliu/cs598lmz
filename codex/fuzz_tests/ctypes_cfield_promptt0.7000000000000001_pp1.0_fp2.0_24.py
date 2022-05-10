import ctypes
# Test ctypes.CField
from ctypes import *
from ctypes.test import is_resource_enabled

if is_resource_enabled("printing"):
    from ctypes import _simple_init
    _simple_init(1)

from ctypes import c_byte, c_ubyte, c_short, c_ushort, c_int, c_uint, \
     c_long, c_ulong, c_longlong, c_ulonglong, c_float, c_double
from ctypes import BigEndianStructure, LittleEndianStructure, \
     Union, Structure, Array, _SimpleCData
from ctypes import _Pointer, POINTER, _CFuncPtr, CFUNCTYPE
from ctypes import _c_functype_cache

from ctypes import ArgumentError
import sys, unittest

if sys.platform == "win32":
    from ctypes import WINFUNCTYPE, WINFUNCTYPE

from ctypes import _cast_addr

class X(Structure):
    _fields_ = [("a", c_int)]

class
