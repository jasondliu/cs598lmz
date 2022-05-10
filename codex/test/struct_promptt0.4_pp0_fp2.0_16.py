import _struct
# Test _struct.Struct

import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct_error(self):
        # Issue #7995: struct.error should be an instance of ValueError
        self.assertTrue(issubclass(struct.error, ValueError))

    def test_struct_pack_error(self):
        # Issue #7995: struct.error should be an instance of ValueError
        self.assertTrue(issubclass(struct.error, ValueError))

    def test_struct_unpack_error(self):
        # Issue #7995: struct.error should be an instance of ValueError
        self.assertTrue(issubclass(struct.error, ValueError))

    def test_struct_unpack_from_error(self):
        # Issue #7995: struct.error should be an instance of ValueError
        self.assertTrue(issubclass(struct.error, ValueError))

