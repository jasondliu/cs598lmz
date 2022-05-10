import _struct
# Test _struct.Struct(format).unpack(data)
#
# Note: This version of the test is used to validate that the C code is
#       properly handling alignment.
#
# See also: stropmodule.c

import sys
import string

from test import support

import unittest
from test.support import bigmemtest

class StructTest(unittest.TestCase):
    def test_struct_unpack(self):
        # Test _struct.Struct(format).unpack(data)
        #
        # See also: stropmodule.c
        #
        # Note: This version of the test is used to validate that the C code is
        #       properly handling alignment.

        # Alignment of 4-byte ints
        self.assertEqual(_struct.Struct('i').unpack(b'\x00\x00\x00\x00'), (0,))
        self.assertEqual(_struct.Struct('i').unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(_struct.Struct('i
