import _struct
# Test _struct.Struct

import sys
import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct_doc(self):
        self.assertEqual(_struct.Struct.__doc__,
                         "Compile a struct format string to return a Struct object")

    def test_struct_unpack_doc(self):
        self.assertEqual(_struct.Struct.unpack.__doc__,
                         "Return a tuple containing values unpacked according to the format string.")

    def test_struct_unpack_from_doc(self):
        self.assertEqual(_struct.Struct.unpack_from.__doc__,
                         "Return a tuple containing values unpacked according to the format string.\n"
                         "The buffer\'s size in bytes must be calcsize().")

    def test_struct_pack_doc(self):
        self.assertEqual(_struct.Struct.pack.__doc__,
                         "Return a bytes object containing the values v1, v2, ... packed according to the format string.")

    def test_struct_pack_
