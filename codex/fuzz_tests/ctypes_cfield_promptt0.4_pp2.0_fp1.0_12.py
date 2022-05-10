import ctypes
# Test ctypes.CField.
#
# This test case is based on the _ctypes test module cfield.py.

import unittest
from test import support

import _ctypes_test

class CFieldTestCase(unittest.TestCase):
    def test_cfield(self):
        # Test ctypes.CField.
        #
        # This test case is based on the _ctypes test module cfield.py.
        #
        # Test the CField class.
        #
        # The CField class is used to describe the fields of a Structure
        # or Union.  It's used to access the fields of a Structure or Union
        # instance, and to create the _fields_ attribute of a Structure
        # subclass.
        #
        # It's also used for the _fields_ attribute of the Structure
        # base class.  This is a little bit different:  The _fields_
        # attribute of the Structure base class is a sequence of CField
        # instances, but the _fields_ attribute of a Structure subclass
        # is a sequence of tuples, containing the CField instance and
       
