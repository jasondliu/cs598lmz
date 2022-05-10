import _struct
# Test _struct.Struct
#
# The following structs should be able to roundtrip all basic python types
#
#     b:  signed char
#     B:  unsigned char
#     h:  signed short
#     H:  unsigned short
#     i:  signed int
#     I:  unsigned int
#     l:  signed long
#     L:  unsigned long
#     f:  float
#     d:  double
#     s:  char[]
#     p:  char[]
#     P:  void *

import sys
import unittest
from test import support

# If these don't work, nothing will
import _struct
import struct

class StructTestCase(unittest.TestCase):
    def test_struct_error(self):
        self.assertRaises(struct.error, _struct.Struct, 'z')
        self.assertRaises(struct.error, _struct.Struct, 'Pz')

