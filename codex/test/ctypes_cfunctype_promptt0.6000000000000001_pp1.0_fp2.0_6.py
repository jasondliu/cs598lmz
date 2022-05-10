import ctypes
# Test ctypes.CFUNCTYPE(), ctypes.py_object, ctypes.cast(),
# ctypes.addressof(), ctypes.POINTER()
import _ctypes_test

from ctypes import Structure, Union
from ctypes import c_int, c_short, c_byte, c_double, c_char, c_char_p
from ctypes import c_float, c_long, c_longlong, c_ulong, c_ulonglong
from ctypes import c_ubyte, c_ushort
from ctypes import sizeof, alignment
from ctypes import POINTER, pointer, byref

from ctypes import CFUNCTYPE

from ctypes import _Pointer

from sys import getrefcount as grc

try:
    unicode
except NameError:
    unicode = str

################################################################
# test class using the new buffer interface

class X(object):
    def __init__(self, buffer):
        self._buffer = buffer
    def __len__(self):
        return len(self._buffer)
