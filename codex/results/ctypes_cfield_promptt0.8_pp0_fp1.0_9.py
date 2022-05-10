import ctypes
# Test ctypes.CField
#
# This test is skipped if the compiler is incompatible with
# ctypes.
#
import unittest
from test import test_support

class CFieldTestCase(unittest.TestCase):
    def test_cfield(self):
        # verify that CPointer and CField get self.from_param correctly
        class POINTER(ctypes.c_long):
            _type_ = 'l'
            def _check_retval_(self):
                return self
            def from_param(cls, value):
                if isinstance(value, int):
                    return cls(value)
                return ctypes.c_long.from_param(value)
            from_param = classmethod(from_param)
        ctypes.POINTER = POINTER

        class Record(ctypes.Structure):
            _fields_ = [('x', ctypes.c_int, 2)]

        class S(ctypes.Structure):
            _fields_ = [('p', ctypes.POINTER(Record))]

        self.assertEqual(ctypes.c_int
