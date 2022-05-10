import ctypes
# Test ctypes.CField
assert issubclass(ctypes.CField, ctypes._SimpleCData)

# Test Field.from_param() for a few classes

from ctypes import *

from test import support

from ctypes import _testcapi
from ctypes.wintypes import HANDLE, LPCWSTR
from ctypes import (
    _check_retval_, ArgumentError, _CFuncPtr, addressof,
    sizeof, py_object, Structure, POINTER
)

from ctypes.util import find_library
msvcrt = find_library("msvcrt")


class X(Union):
    _fields_ = [("a", c_int)]

class Z(Structure):
    _fields_ = [("a", c_int)]


class Y(Structure):
    _fields_ = [("p", POINTER(c_int))]


class POINT(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int)]


def test(typ):
    libc = cdll.
