import ctypes
# Test ctypes.CFUNCTYPE with nested prototypes
from ctypes import *
import _ctypes_test

prototype = CFUNCTYPE(c_int, c_int, c_int, c_int)
class X(Union):
    _fields_ = [("x", prototype),
                ("y", prototype)]

lib = CDLL(_ctypes_test.__file__)

