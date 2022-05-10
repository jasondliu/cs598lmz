import _struct
# Test _struct.Struct

import unittest
import sys
import struct
import test.test_support

# The struct module uses PyArg_ParseTuple() to parse the format string,
# which is not available in the restricted environment.
#@unittest.skipUnless(not test.test_support.is_restricted('struct'),
#                     'test needs unrestricted struct')

# The struct module uses PyArg_ParseTuple() to parse the format string,
# which is not available in the restricted environment.
@unittest.skipUnless(not test.test_support.is_restricted('struct'),
                     'test needs unrestricted struct')
class StructTestCase(unittest.TestCase):
    def test_struct(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, struct.calcsize('i'))

    def test_pack(self):
        s = _struct.Struct('i')
        self.assertEqual(s.pack(1), struct.pack('i', 1))

    def test_unpack(self):
        s = _
