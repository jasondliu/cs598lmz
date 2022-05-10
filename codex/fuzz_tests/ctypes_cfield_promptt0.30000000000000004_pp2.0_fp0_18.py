import ctypes
# Test ctypes.CField.from_address()

import unittest
from test import support

class CFieldTestCase(unittest.TestCase):
    def test_from_address(self):
        # Test that ctypes.CField.from_address() works correctly.
        #
        # This is a regression test for issue #11863.
        #
        # The issue is that the CField.from_address() method was not
        # correctly handling the case where the address of the field
        # was not aligned on a pointer boundary.  This would cause
        # the from_address() method to return an incorrect value.
        #
        # The test below creates a structure with a field that is not
        # aligned on a pointer boundary.  It then verifies that the
        # from_address() method returns the correct value.
        #
        # The test is written in such a way that it should work
        # correctly on any architecture.
        class S(ctypes.Structure):
            _fields_ = [('a', ctypes.c_char),
                        ('b', ctypes.c_int)]


