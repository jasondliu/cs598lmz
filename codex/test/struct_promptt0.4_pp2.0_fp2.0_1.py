import _struct
# Test _struct.Struct

from test import test_support
import unittest

class StructTest(unittest.TestCase):

    def test_struct_doc(self):
        self.assertEqual(
            _struct.Struct.__doc__,
            "Compile a struct format string, returning a Struct object."
        )

    def test_unpack_doc(self):
        self.assertEqual(
            _struct.Struct.unpack.__doc__,
            "Return a tuple containing values unpacked according to the format string."
        )

    def test_unpack_from_doc(self):
        self.assertEqual(
            _struct.Struct.unpack_from.__doc__,
            "Return a tuple containing values unpacked according to the format string."
        )

    def test_pack_doc(self):
        self.assertEqual(
            _struct.Struct.pack.__doc__,
            "Return a string containing values packed according to the format string."
        )

