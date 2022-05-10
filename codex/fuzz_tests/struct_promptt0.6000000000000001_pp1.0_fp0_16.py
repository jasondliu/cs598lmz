import _struct
# Test _struct.Struct.

import unittest

from test import test_support
from test.test_support import bigaddrspacetest

# Helper functions

def b(s):
    return s.encode("latin-1")

def s(b):
    return b.decode("latin-1")

class StructTest(unittest.TestCase):

    def test_unpack_from(self):
        # SF buf 1647541: struct.unpack_from() segfaults
        # http://bugs.python.org/issue17482
        # Tests for segfault/buffer overrun
        s = _struct.Struct(b('=I'))
        self.assertRaises(struct.error, s.unpack_from, b(''), 0)
        self.assertRaises(struct.error, s.unpack_from, b('xxxx'), 0)
        self.assertRaises(struct.error, s.unpack_from, b('xxxx'), 1)
        self.assertRaises(struct.error, s.unpack_from, b('
