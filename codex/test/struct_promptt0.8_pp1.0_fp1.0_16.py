import _struct
# Test _struct.Struct class.

# XXX This is mainly a test of the iterative API.  We should probably
# XXX create tests for the others, using the iterative API as the model.

import _struct as struct
import sys
import unittest
from test import test_support

class StructTestCase(unittest.TestCase):

    def test_iter_empty(self):
        # Test iteration on empty format
        fmt = struct.Struct('')
        s = fmt.pack()
        self.assertEqual(len(s), 0)
        self.assertEqual(fmt.size, 0)
        self.assertEqual(list(fmt.get_unpack_iter(s)), [])

    def test_format_discovery(self):
        # Test automatic format discovery
        fmt = struct.Struct('xx2s3i')
        self.assertEqual(fmt.format, '=xx2si3i')
        s = fmt.pack('ab', 1, 2, 3)
        self.assertEqual(len(s), fmt.size)
