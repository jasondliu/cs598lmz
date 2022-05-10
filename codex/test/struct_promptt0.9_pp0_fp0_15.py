import _struct
# Test _struct.Struct() format string argument.
# Argument is a string containing the format of the argument to pack/unpack.
# This string is the same as the usual Struct class except that it uses
# '<' and '>' instead of '@' to specify native endianness.


class StructTestCase(unittest.TestCase):

    def test_compare(self):
        # The '>' format is the default with the old struct.Struct class.
        with self.assertRaises(AttributeError):
            struct.Struct('>i') == struct.Struct('>i')
        self.assertEqual(struct.Struct('>i'), struct.Struct('>i'))

    def test_new_struct_string(self):
        S = struct.Struct('>i')
        S2 = _struct.Struct('>i')
        self.assertEqual(S.format, S2.format)


# This test class contains test cases for _struct.Struct using the
# new_struct_string test fixture.
