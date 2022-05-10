import ctypes
# Test ctypes.CFUNCTYPE
#
# This is a test for the ctypes.CFUNCTYPE function.
#
# The test is a bit more complicated than usual, because it uses the
# Python C API to create a Python function object from a C function
# pointer.

import unittest
from test import support

class CFuncPtrTestCase(unittest.TestCase):
    def test_CFuncPtr(self):
        # create a C function pointer from a function
        def func(arg):
            return arg * 2
        cfunc = ctypes.CFUNCTYPE(ctypes.c_int)(func)

        # create a Python function object from the C function pointer
        PyCFunctionObject = ctypes.pythonapi.PyCFunction_Type
        PyCFunction_NewEx = ctypes.pythonapi.PyCFunction_NewEx
        PyCFunction_NewEx.restype = ctypes.py_object
        PyCFunction_NewEx.argtypes = [ctypes.py_object, ctypes.py_object,
                                      ctypes.py_object]
        args = (ct
