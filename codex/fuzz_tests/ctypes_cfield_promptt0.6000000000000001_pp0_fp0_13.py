import ctypes
# Test ctypes.CField()
#
# This tests the ctypes.CField() function
#
# The CField() function is used to create a field descriptor
# for a given field in a C structure.  The descriptor
# can be used to access the field.

import unittest
from test import test_support

try:
    import _ctypes_test
except ImportError:
    _ctypes_test = None

class CFieldTestCase(unittest.TestCase):

    @unittest.skipUnless(_ctypes_test, 'requires _ctypes')
    def test_descriptor_access(self):
        # The descriptor object has a '__get__' and '__set__' method
        # which can be used to get or set the value of the field.
        # The descriptor object is usually created by CField(),
        # but can also be instantiated directly.
        #
        # The '__get__' method takes an instance of the structure,
        # and returns the value of the field.  If the field is not
        # present in the instance, an AttributeError is raised.
