import _struct
# Test _struct.Struct

from test.test_support import run_unittest
from test import mapping_tests
import sys

class StructTest(mapping_tests.BasicTestMappingProtocol):

    type2test = _struct.Struct
    basetype = _struct.Struct
    basetype2 = type

    def _reference(self):
        return _struct.Struct("")

    def _empty_mapping(self):
        return _struct.Struct("")

    def test_basic_struct(self):
        s = _struct.Struct("i")
        self.assertEqual(s.size, 4)
        self.assertEqual(s.format, "i")
        self.assertEqual(s.__doc__,
            "Compiled struct object\n"
            "    <format> : str\n"
            "    <ord> : str\n"
            "    <size> : int"
            )

    def test_big_endian_format(self):
        s = _struct.Struct(">i")
        self.assertEqual(s.size
