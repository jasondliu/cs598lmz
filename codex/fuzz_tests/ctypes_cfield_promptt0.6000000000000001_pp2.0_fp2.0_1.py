import ctypes
# Test ctypes.CField.
#
# This test is derived from a bug report in which a subclass of Structure
# failed to initialize the '_fields_' attribute.

import unittest
from test import test_support

# Build a Structure subclass with a _fields_ attribute.
class Struct(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class TestCField(unittest.TestCase):
    def test_cfield(self):
        # Create an instance of the subclass.
        s = Struct()

        # Check that the _fields_ attribute is initialized.
        self.failUnless(s._fields_ == [("a", ctypes.c_int)])

        # Check that the instance is initialized.
        self.failUnless(s.a == 0)

def test_main():
    test_support.run_unittest(TestCField)

if __name__ == "__main__":
    test_main()
