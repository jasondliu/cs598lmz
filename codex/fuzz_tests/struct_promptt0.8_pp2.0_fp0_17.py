import _struct
# Test _struct.Struct.iter_unpack()

import struct
import unittest
from test.support import run_unittest, HAVE_DOCSTRINGS

class StructIterUnpackTests(unittest.TestCase):

    @unittest.skipUnless(HAVE_DOCSTRINGS, 'test needs docstrings')
    def test_docstring(self):
        self.assertEqual(_struct.Struct.iter_unpack.__doc__,
                         struct.Struct.iter_unpack.__doc__)

    def test_basic(self):
        s = _struct.Struct(">2H")
        input = b"\x00\x01\x00\x02\x00\x03\x00\x04"
        output = [(1, 2), (3, 4)]
        it = s.iter_unpack(input)
        self.assertEqual(list(it), output)

    def test_overflow(self):
        s = _struct.Struct(">2H")
        input = b"\x00\x01\x00\x02\x00
