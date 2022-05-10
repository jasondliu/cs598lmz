import ctypes
# Test ctypes.CFUNCTYPE and ctypes.py_object.
# This is a test case for http://bugs.python.org/issue7561.
from ctypes import *

from ctypes.test.test_pickling import needs_unicode

from test import test_support
import unittest
import pickle

libc = CDLL(test_support.TESTFN)

# Some versions of libc on windows seem to require that the
# argtypes and restype be set *before* the function is used.  This
# is a copy of c_functype_cache, modified so that the argtypes and
# restype can be set before the function is called.
class c_functype_cache_settable(c_functype_cache):
    def __init__(self, func, restype=None, argtypes=None, errcheck=None):
        c_functype_cache.__init__(self, func, errcheck)
        self._restype_ = restype
        self._argtypes_ = argtypes

    def __call__(self, *args):
        func
