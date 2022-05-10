import _struct
# Test _struct.Struct

import unittest
from test.support import bigaddrspacetest
from test.support import import_helper

struct = import_helper.import_module('struct')

class StructTestCase(unittest.TestCase):
    def test_format_size(self):
        # Test the format_size() function
        self.assertEqual(struct.calcsize(b""), 0)
        self.assertEqual(struct.calcsize(b"<"), 0)
        self.assertEqual(struct.calcsize(b"<B"), 1)
        self.assertEqual(struct.calcsize(b"<BB"), 2)
        self.assertEqual(struct.calcsize(b"<BBB"), 3)
        self.assertEqual(struct.calcsize(b"<BBBB"), 4)
        self.assertEqual(struct.calcsize(b"<BBBBB"), 5)
        self.assertEqual(struct.calcsize(b"<BBBBBB"), 6)
