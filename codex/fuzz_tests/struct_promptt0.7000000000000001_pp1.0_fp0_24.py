import _struct
# Test _struct.Struct().pack()

import _struct
import sys
import unittest
from test import support
from test.support import bigmemtest

struct_class = _struct.Struct

class StructTestCase(unittest.TestCase):

    def test_pack_into_non_writable_buffer(self):
        with self.assertRaises(TypeError):
            _struct.Struct("i").pack_into(memoryview(bytearray(4)), 0, 0)

    def test_unpack_from_non_readable_buffer(self):
        with self.assertRaises(TypeError):
            _struct.Struct("i").unpack_from(memoryview(bytearray(4)))

    def test_pack_into_resizeable_buffer(self):
        with self.assertRaises(TypeError):
            _struct.Struct("i").pack_into(bytearray(4), 0, 0)

    def test_unpack_from_resizeable_buffer(self):
        with self.assertRaises(TypeError):
            _struct.Struct("i
