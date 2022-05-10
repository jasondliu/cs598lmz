import ctypes
# Test ctypes.CField instance's tp_descr_set slot.
from ctypes import *

# Import Test GTK to initialize gettext
import test

import sys

if sys.platform == "win32":
    from ctypes.wintypes import BOOL
else:
    BOOL = c_int

class POINT(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int)]

class RECT(Structure):
    _fields_ = [("left"  , c_int),
                ("top"   , c_int),
                ("right" , c_int),
                ("bottom", c_int)]

def test_descr(descr, x, y):
    if descr(x) == descr(y):
        raise RuntimeError("descr(%r) == descr(%r)" % (x, y))

if sys.platform == "win32":
    def POINT_from_LPARAM(x, y):
        return POINT.from_address(x.value)
else:
   
