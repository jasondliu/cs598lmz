import _struct
# Test _struct.Struct().unpack_from()

import unittest
from test import support
import sys

# This test assumes native byte order is little endian
native_is_le = sys.byteorder == 'little'

# Test data
data_le = b'\x12\x34\x56\x78\x9a\xbc\xde\xf0'
data_be = b'\x12\x34\x56\x78\x9a\xbc\xde\xf0'[::-1]

# Test structs
s_le = _struct.Struct('<Q')
s_be = _struct.Struct('>Q')

# Expected results
if native_is_le:
    expected_le = 0x123456789abcdef0
    expected_be = 0xf0debc9a78563412
else:
    expected_le = 0xf0debc9a78563412
    expected_be = 0x123456789abcdef0

class StructTest(unittest.TestCase):

    def test_un
