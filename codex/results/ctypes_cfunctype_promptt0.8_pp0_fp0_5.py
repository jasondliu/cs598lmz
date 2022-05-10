import ctypes
# Test ctypes.CFUNCTYPE for returning a pointer type.
from ctypes.test import need_symbol

import _ctypes_test
dll = ctypes.CDLL(_ctypes_test.__file__)

# This function is defined in ctypes_others.c
GetString = dll._testfunc_GetString
GetString.restype = ctypes.POINTER(ctypes.c_char)

need_symbol('c_wchar_p')
GetWString = dll._testfunc_GetWString
GetWString.restype = ctypes.POINTER(ctypes.c_wchar)

s = GetString()
if s.contents.value != "Hello World":
    raise RuntimeError("GetString() returned %s" % s.contents.value)

s = GetWString()
if s.contents.value != u"Hello World":
    raise RuntimeError("GetWString() returned %s" % repr(s.contents.value))
