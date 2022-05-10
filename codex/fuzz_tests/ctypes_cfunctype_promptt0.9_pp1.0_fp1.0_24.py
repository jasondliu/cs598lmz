import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import *
import _ctypes_test
from _ctypes_test import func
from _ctypes_test import getargs
from _ctypes_test import getfloat

from ctypes import wintypes

from ctypes import cdll, util

from ctypes import oledll, oleaut

from ctypes import coml2api
from ctypes.coml2api import *

from ctypes import test

from ctypes import _endian
try:
    _ctypes_test.have_longlong
except AttributeError:
    import sys
    print("_ctypes_test does not have a have_longlong attribute")
    sys.exit(1)


################################################################
#
#
if _ctypes_test.have_longlong:
    longlong_max = 2 ** 63 - 1
    longlong_min = -2 ** 63
    ulonglong_max = 2 ** 64 - 1

    class TestLongLong(unittest.TestCase):
        def test_longlong_max(self):
            value = _ctypes_test
