import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import *
from ctypes.test import is_resource_enabled

from ctypes import _testcapi

import unittest
from test import test_support
from test import string_tests

################################################################
# ctypes callback tests, using the _testcapi module

if is_resource_enabled("printing"):
    import warnings
    warnings.filterwarnings("ignore",
                            message="comparing signed and unsigned integers",
                            category=RuntimeWarning)

def callback(index, name, calls):
    calls["index"] = index
    calls["name"] = name
    return index

CB_FUNC = CFUNCTYPE(c_int, c_int, c_char_p)

class CallbackTestCase(unittest.TestCase):

    def test_simple(self):
        _testcapi.set_callback(CB_FUNC(callback), 42)
        calls = {}
        res = _testcapi.call_callback("arg", calls)
        self.assertEqual(res, 42)
        self.assertE
