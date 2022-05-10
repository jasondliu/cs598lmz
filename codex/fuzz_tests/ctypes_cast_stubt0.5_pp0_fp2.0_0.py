import ctypes
ctypes.cast(0, ctypes.py_object)

# ______________________________________________________________________

from numba.tests.test_support import TestCase
from numba import *
from numba.decorators import jit
from numba import typesystem
from numba.minivect import minitypes
from numba.minivect.minitypes import *
import numpy

# ______________________________________________________________________

class TestTypes (TestCase):
    def test_typesystem (self):
        """
        Check that the type system is working.
        """
        def func(x, y):
            return x + y
        func = jit(argtypes=[double, double], restype=double)(func)
        self.assertEqual(func(1.0, 2.0), 3.0)

    def test_typesystem_array (self):
        """
        Check that the type system is working with arrays.
        """
        def func(x, y):
            return x + y
        func = jit(argtypes=[double[:], double[:]], restype=double[:])(func)

