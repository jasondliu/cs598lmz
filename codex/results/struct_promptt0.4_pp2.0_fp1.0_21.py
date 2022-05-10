import _struct
# Test _struct.Struct

# This test is not complete.  It checks some key aspects of the _struct
# module, but not all.

import struct
import sys
import unittest
from test import support

class StructTestCase(unittest.TestCase):
    def test_struct_doc(self):
        # Test the docstrings of the struct module
        self.assertTrue(struct.__doc__)
        self.assertTrue(struct.Struct.__doc__)
        self.assertTrue(struct.pack.__doc__)
        self.assertTrue(struct.unpack.__doc__)
        self.assertTrue(struct.iter_unpack.__doc__)

    def test_struct_module(self):
        # Test the struct module
        self.assertEqual(struct.calcsize('i'), 4)
        self.assertEqual(struct.calcsize('ii'), 8)
        self.assertEqual(struct.calcsize('i'*100), 400)
        self.assertEqual(struct.calcsize('i'*1000), 4000)
        self
