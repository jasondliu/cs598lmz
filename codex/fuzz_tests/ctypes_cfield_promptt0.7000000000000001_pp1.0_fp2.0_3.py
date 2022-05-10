import ctypes
# Test ctypes.CField.from_address()
# http://bugs.python.org/issue15984

import unittest
import warnings

from test import support

libc = ctypes.CDLL(support.TESTFN)

class POINTER(ctypes.c_int):
    _type_ = 'P'

class Test(unittest.TestCase):
    def test_from_address(self):
        class S(ctypes.Structure):
            _fields_ = [('a', ctypes.c_int)]

        ptr = ctypes.pointer(S.from_address(ctypes.addressof(libc.printf)))
        self.assertRaises(TypeError, ctypes.CField.from_address, ptr, S)
        self.assertRaises(TypeError, ctypes.CField.from_address, ptr, 'struct S')

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            ctypes.CField.from_address(ptr, ctypes.POINTER(S))
            self.assert
