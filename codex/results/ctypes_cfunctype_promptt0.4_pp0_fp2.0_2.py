import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is a bit different from the others in that it tests a
# feature of ctypes, not of Python.  It also tests a feature that
# isn't documented in the ctypes docs, so it's a bit of a hack.

import unittest
from test import test_support

try:
    ctypes
except NameError:
    raise unittest.SkipTest("ctypes not available")

# This function is defined in Python/ceval.c.
_PyEval_CallFunction = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object,
                                        ctypes.py_object)(
    ctypes.pythonapi.PyEval_CallFunction)

class CFunctionTestCase(unittest.TestCase):

    def test_call_function(self):
        # This is a bit of a hack, but it tests the feature.  The
        # function PyEval_CallFunction takes a variable number of
        # arguments.  The first argument is a Python callable object,
        # and the second is a tuple of
