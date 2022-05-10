import _struct
# Test _struct.Struct

class StructTestCase(unittest.TestCase):
    def test_struct(self):
        self.assertEqual(StructTestCase._fmt("@"), "native")
        self.assertEqual(StructTestCase._fmt("="), "native")
        self.assertEqual(StructTestCase._fmt("<"), "little")
        self.assertEqual(StructTestCase._fmt(">"), "big")
        self.assertEqual(StructTestCase._fmt("!"), "network")

        self.assertEqual(StructTestCase._fmt("x"), "pad byte")
        self.assertEqual(StructTestCase._fmt("c"), "char")
        self.assertEqual(StructTestCase._fmt("b"), "signed char")
        self.assertEqual(StructTestCase._fmt("B"), "unsigned char")
        self.assertEqual(StructTestCase._fmt("?"), "bool")
        self.assertEqual(StructTestCase._fmt("h"), "short")
        self.assertEqual(StructTest
